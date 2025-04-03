import http.server
import socketserver
import os

LOG_FILE = "/data/sedra.log"

class LogHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/logs":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            if os.path.exists(LOG_FILE):
                with open(LOG_FILE, "r") as f:
                    self.wfile.write(f.read().encode())
            else:
                self.wfile.write(b"No logs yet.")
        else:
            return http.server.SimpleHTTPRequestHandler.do_GET(self)

if __name__ == "__main__":
    os.chdir("/app/public")
    with socketserver.TCPServer(("", 80), LogHandler) as httpd:
        print("Serving on port 80...")
        httpd.serve_forever()
