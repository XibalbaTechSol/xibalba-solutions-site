import http.server
import socketserver
import urllib.parse
import smtplib
from email.mime.text import MIMEText
import os
import sys

# --- Configuration ---
PORT = 8000
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

# SMTP Configuration (Recommended to use environment variables)
# If running locally, you might need to use a real SMTP server like Gmail (App Password required)
# or a local postfix server.
SMTP_SERVER = os.environ.get("SMTP_SERVER", "localhost")
SMTP_PORT = int(os.environ.get("SMTP_PORT", "587"))
SMTP_USER = os.environ.get("SMTP_USER", "")
SMTP_PASS = os.environ.get("SMTP_PASS", "")
FROM_EMAIL = os.environ.get("FROM_EMAIL", "contact@xibalbasolutions.com")
RECIPIENTS = ["jacob@xibalbasolutions.com", "jacob.v.universe@gmail.com"]

class XibalbaHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

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
                message = fields.get('message', [''])[0]

                print(f"Received contact request from: {name} <{email}>")

                # Construct the email body
                email_body = f"""
New Contact Form Submission from Xibalba Solutions Website

----------------------------------------------------------
Name:     {name}
Email:    {email}
Interest: {interest}
----------------------------------------------------------

Message:
{message}

----------------------------------------------------------
Submitted via local self-hosted handler.
"""
                
                msg = MIMEText(email_body)
                msg['Subject'] = f"AI Inquiry: {name} - {interest}"
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

                # On success, redirect to the thank-you page
                self.send_response(303)
                self.send_header('Location', '/thank-you.html')
                self.end_headers()

            except Exception as e:
                print(f"Error handling contact form: {e}", file=sys.stderr)
                self.send_response(500)
                self.end_headers()
                self.wfile.write(f"An internal error occurred: {str(e)}".encode())
        else:
            self.send_error(404, "File not found")

if __name__ == "__main__":
    # Ensure we are in the correct directory
    os.chdir(DIRECTORY)
    
    # Allow port reuse to avoid "Address already in use" errors during development
    socketserver.TCPServer.allow_reuse_address = True
    
    with socketserver.TCPServer(("", PORT), XibalbaHandler) as httpd:
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
