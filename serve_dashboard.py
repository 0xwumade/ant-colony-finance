"""
serve_dashboard.py — Serve the dashboard with environment variables injected

This script reads the treasury address from .env and injects it into
the dashboard HTML before serving it.

Usage:
    python serve_dashboard.py
    # Then open http://localhost:8000
"""
import os
from http.server import HTTPServer, SimpleHTTPRequestHandler
from dotenv import load_dotenv

load_dotenv()

TREASURY_ADDRESS = os.getenv('TREASURY_ADDRESS', '0x0000000000000000000000000000000000000000')

class DashboardHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/' or self.path == '/index.html':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            
            with open('index.html', 'r', encoding='utf-8') as f:
                html = f.read()
            
            # Inject treasury address
            html = html.replace(
                "const treasuryAddress = 'YOUR_TREASURY_ADDRESS_HERE';",
                f"const treasuryAddress = '{TREASURY_ADDRESS}';"
            )
            
            self.wfile.write(html.encode('utf-8'))
        else:
            super().do_GET()

if __name__ == '__main__':
    PORT = 8000
    print(f"🐜 Ant Colony Finance Dashboard")
    print(f"   Treasury: {TREASURY_ADDRESS}")
    print(f"   Server:   http://localhost:{PORT}")
    print(f"\nPress Ctrl+C to stop")
    
    server = HTTPServer(('localhost', PORT), DashboardHandler)
    server.serve_forever()
