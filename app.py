from http.server import BaseHTTPRequestHandler, HTTPServer

class HelloHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(b"Hello World from CodePipeline CI/CD!")

if __name__ == "__main__":
    server_address = ('', 80)
    httpd = HTTPServer(server_address, HelloHandler)
    print("Starting server on port 80...")
    httpd.serve_forever()
