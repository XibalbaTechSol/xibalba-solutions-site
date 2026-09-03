import http.server
import socketserver
import urllib.parse
import smtplib
from email.mime.text import MIMEText
import os
import sys
from dotenv import load_dotenv

# Load environment variables from .env if present
load_dotenv()

# --- Configuration ---
PORT = int(os.environ.get("PORT", 8000))
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

# SMTP Configuration (Recommended to use environment variables)
# If running locally, you might need to use a real SMTP server like Gmail (App Password required)
# or a local postfix server.
SMTP_SERVER = os.environ.get("SMTP_SERVER", "localhost")
SMTP_PORT = int(os.environ.get("SMTP_PORT", "587"))
SMTP_USER = os.environ.get("SMTP_USER", "")
SMTP_PASS = os.environ.get("SMTP_PASS", "")
FROM_EMAIL = os.environ.get("FROM_EMAIL", "relay@xibalbasolutions.com")
RECIPIENTS = ["jacob.v.universe@gmail.com"]

# The static pages are served from GitHub Pages (a different origin than this backend, which
# only handles /contact); the form fetch()'s response needs this to be readable cross-origin.
ALLOWED_ORIGIN = os.environ.get("ALLOWED_ORIGIN", "https://xibalbatechsol.github.io")

class XibalbaHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def do_OPTIONS(self):
        # CORS preflight -- browsers only send this for non-"simple" requests, but the fetch
        # client's headers/method are simple enough to skip it today; handled anyway so this
        # keeps working if that client ever adds a custom header.
        self.send_response(204)
        self.send_header('Access-Control-Allow-Origin', ALLOWED_ORIGIN)
        self.send_header('Access-Control-Allow-Methods', 'POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()

    def do_POST(self):
        if self.path == '/contact':
            try:
                # Read form data
                content_length = int(self.headers['Content-Length'])
                post_data = self.rfile.read(content_length).decode('utf-8')
                fields = urllib.parse.parse_qs(post_data)

                # Extract fields safely
                name = fields.get('name', [''])[0]
                email = fields.get('email', [''])[0]
                interest = fields.get('interest', [''])[0]
                subject = fields.get('subject', ['Inquiry'])[0]
                message = fields.get('message', [''])[0]
                source_page = fields.get('source_page', ['Unknown'])[0]

                print(f"Received contact request from: {name} <{email}> via {source_page}")

                # Construct the email body
                email_body = f"""
--- SYSTEM CONTEXT ---
Source Page: {source_page}
Timestamp:   {self.log_date_time_string()}
Relay:       Xibalba Sovereign Handler v2.0

--- USER DATA ---
Name:        {name}
Email:       {email}
Subject:     {subject}
Interest:    {interest}

--- MESSAGE ---
{message}

----------------------------------------------------------
This message was relayed via the Xibalba local server.
"""
                
                msg = MIMEText(email_body)
                msg['Subject'] = f"Contact: {name} - {subject}"
                msg['From'] = FROM_EMAIL
                msg['To'] = ", ".join(RECIPIENTS)

                # Send via SMTP
                if SMTP_USER and SMTP_PASS:
                    # authenticated SMTP (e.g. Gmail, SendGrid, etc.)
                    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
                        server.starttls()
                        server.login(SMTP_USER, SMTP_PASS)
                        server.send_message(msg)
                else:
                    # local unauthenticated SMTP (e.g. local postfix)
                    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
                        server.send_message(msg)

                # On success, redirect to the thank-you page. This targets the backend's own
                # relative path, which only matters for a no-JS form submit (the fetch() path in
                # main.js only checks response.ok and never navigates on it).
                self.send_response(303)
                self.send_header('Location', '/thank-you.html')
                self.send_header('Access-Control-Allow-Origin', ALLOWED_ORIGIN)
                self.end_headers()

            except Exception as e:
                print(f"Error handling contact form: {e}", file=sys.stderr)
                self.send_response(500)
                self.send_header('Access-Control-Allow-Origin', ALLOWED_ORIGIN)
                self.end_headers()
                self.wfile.write(f"An internal error occurred: {str(e)}".encode())
        else:
            self.send_error(404, "File not found")

if __name__ == "__main__":
    # Ensure we are in the correct directory
    os.chdir(DIRECTORY)
    
    # Allow port reuse to avoid "Address already in use" errors during development
    socketserver.ThreadingTCPServer.allow_reuse_address = True

    # Plain TCPServer handles one connection at a time -- any client that opens a connection
    # and doesn't send/finish promptly (a slow client, an idle keep-alive, a proxy health
    # check) blocks every other request, including /contact, until it closes. That's a real
    # problem once this is reachable from the public internet (Render's edge proxy, browsers
    # doing HTTP keep-alive) rather than only from a single local dev client. Threading fixes
    # it; SimpleHTTPRequestHandler's static-file serving and the /contact handler above don't
    # share mutable state, so per-request threads are safe here.
    socketserver.ThreadingTCPServer.daemon_threads = True
    with socketserver.ThreadingTCPServer(("", PORT), XibalbaHandler) as httpd:
        print(f"--- Xibalba Solutions Local Server ---")
        print(f"Serving files from: {DIRECTORY}")
        print(f"Contact endpoint ready at: http://localhost:{PORT}/contact")
        print(f"Listening on port: {PORT}")
        print(f"---------------------------------------")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nShutting down server.")
            httpd.server_close()
