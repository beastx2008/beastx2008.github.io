import os
import requests
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

BASE = "https://lagoslife.eliysites.com"
PORT = 8080
HERE = os.path.dirname(os.path.abspath(__file__))

# One requests session, exactly like the Termux script
session = requests.Session()


class Handler(BaseHTTPRequestHandler):
    def _send(self, status, body, ctype):
        self.send_response(status)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def _proxy(self):
        length = int(self.headers.get("Content-Length") or 0)
        data = self.rfile.read(length) if length else None
        headers = {}
        if self.headers.get("Content-Type"):
            headers["Content-Type"] = self.headers["Content-Type"]
        try:
            r = session.request(
                self.command,
                BASE + self.path,
                data=data,
                headers=headers,
                timeout=15,
            )
            self._send(r.status_code, r.content,
                       r.headers.get("Content-Type", "application/json"))
        except requests.RequestException as e:
            self._send(502, str(e).encode(), "text/plain")

    def do_GET(self):
        if self.path.startswith("/api/"):
            return self._proxy()
        path = os.path.join(HERE, "index.html")
        with open(path, "rb") as f:
            self._send(200, f.read(), "text/html; charset=utf-8")

    def do_POST(self):
        if self.path.startswith("/api/"):
            return self._proxy()
        self._send(404, b"Not found", "text/plain")

    def log_message(self, *args):
        pass


if __name__ == "__main__":
    server = ThreadingHTTPServer(("127.0.0.1", PORT), Handler)
    print(f"Open http://127.0.0.1:{PORT} in your browser")
    print("Press Ctrl+C to stop")
    server.serve_forever()
