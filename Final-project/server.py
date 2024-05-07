import http.server
import socketserver
import termcolor
from pathlib import Path
from urllib.parse import parse_qs, urlparse
import jinja2 as j

PORT = 8080
socketserver.TCPServer.allow_reuse_address = True
class TestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        url_path = urlparse(self.path)
        path = url_path.path
        arguments = parse_qs(url_path.query)
        termcolor.cprint(self.requestline, 'blue')
        if path == "/" or path.startswith("/echo"):
            contents = Path('./html/index.html').read_text()
            self.send_response(200)
        elif path == "/ping":
            pass
        else:
            contents = Path('./html/error.html').read_text()
            # Generating the response message
            self.send_response(404)

        # Define the content-type header:
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(str.encode(contents)))

        # The header is finished
        self.end_headers()
        print("intro seq:", contents)

        # Send the response message
        self.wfile.write(str.encode(contents))

        return


# ------------------------
# - Server MAIN program
# ------------------------
# -- Set the new handler
Handler = TestHandler

# -- Open the socket server
with socketserver.TCPServer(("", PORT), Handler) as httpd:

    print("Serving at PORT", PORT)

    # -- Main loop: Attend the client. Whenever there is a new
    # -- clint, the handler is called
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stopped by the user")
        httpd.server_close()
