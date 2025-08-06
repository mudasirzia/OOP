from http.server import BaseHTTPRequestHandler, HTTPServer

class RH(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Hello World, this is mudasir zia.")


server = HTTPServer(("0.0.0.0", 8000), RH)
server.serve_forever()
