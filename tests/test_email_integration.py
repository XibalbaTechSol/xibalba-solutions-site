import unittest
from unittest.mock import patch, MagicMock
import urllib.parse
import http.client
import threading
import time
import os
import sys

# Import the handler from server.py
# We need to add the directory to sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from server import XibalbaHandler
import socketserver

class TestEmailIntegration(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.port = 8003
        cls.handler = XibalbaHandler
        socketserver.TCPServer.allow_reuse_address = True
        cls.server = socketserver.TCPServer(("", cls.port), cls.handler)
        cls.server_thread = threading.Thread(target=cls.server.serve_forever)
        cls.server_thread.daemon = True
        cls.server_thread.start()
        # Give it a moment to start
        time.sleep(1)

    @classmethod
    def tearDownClass(cls):
        cls.server.shutdown()
        cls.server.server_close()

    @patch('smtplib.SMTP')
    def test_contact_form_submission(self, mock_smtp):
        # Setup mock
        instance = mock_smtp.return_value.__enter__.return_value
        
        # Form data
        data = {
            'name': 'Test User',
            'email': 'test@example.com',
            'subject': 'Custom AI Integration',
            'message': 'Hello, this is a test message.',
            'source_page': 'Test Suite'
        }
        encoded_data = urllib.parse.urlencode(data).encode('utf-8')
        
        # Send POST request
        conn = http.client.HTTPConnection("localhost", self.port)
        headers = {
            "Content-Type": "application/x-www-form-urlencoded",
            "Content-Length": len(encoded_data)
        }
        conn.request("POST", "/contact", body=encoded_data, headers=headers)
        response = conn.getresponse()
        
        # Assertions
        self.assertEqual(response.status, 303)
        self.assertEqual(response.getheader('Location'), '/thank-you.html')
        
        # Verify SMTP call
        self.assertTrue(instance.send_message.called)
        sent_msg = instance.send_message.call_args[0][0]
        payload = sent_msg.get_payload()
        self.assertIn('Test User', payload)
        self.assertIn('test@example.com', payload)
        self.assertIn('Hello, this is a test message.', payload)
        
        print("\n[SUCCESS] Contact form submission validated. Email sending logic verified via Mock SMTP.")

if __name__ == '__main__':
    unittest.main()
