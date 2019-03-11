import http.server


class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(s):
        if s.path == "good":
            s.send_response(200)
            s.send_header("Content-type", "text/plain")
            s.end_headers()
            s.wfile.write(b"A good request")
            return
        s.send_response(400)
        s.send_header("Content-type", "text/plain")
        s.end_headers()
        s.wfile.write(b"A bad request")


httpd = http.server.HTTPServer(('', 8000), MyHandler)
httpd.serve_forever()
