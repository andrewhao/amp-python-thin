import http.server


class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == "good":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"A good request")
            return
        self.send_response(400)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(b"A bad request")


http.server.HTTPServer(('', 8000), MyHandler).serve_forever()
