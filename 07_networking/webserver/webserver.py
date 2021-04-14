from http.server import BaseHTTPRequestHandler, HTTPServer

host = "localhost"
port = 8083

class WebServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<h1>Hello</h1>", "utf-8"))

if __name__ == '__main__':
    server = HTTPServer((host, port), WebServer)

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass

    server.server_close()
