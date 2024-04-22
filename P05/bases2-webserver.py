import http.server
import socketserver
from pathlib import Path
# -- Server network parameters
PORT = 8080
socketserver.TCPServer.allow_reuse_address = True
class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        """This method is called whenever the client invokes the GET method
        in the HTTP protocol request"""
        # Generating the response message
        if self.path == "/":
            contents = Path("./html/index.html").read_text()
            self.send_response(200)
        elif self.path == "/info/A":
            contents = Path("./html/info/A.html").read_text()
            self.send_response(200)
        elif self.path == "/info/C":
            contents = Path("./html/info/C.html").read_text()
            self.send_response(200)
        elif self.path == "/info/G":
            contents = Path("./html/info/G.html").read_text()
            self.send_response(200)
        elif self.path == "/info/T":
            contents = Path("./html/info/T.html").read_text()
            self.send_response(200)
        else:
            contents = Path("./html/error.html").read_text()
            self.send_response(404)

        # Define the content-type header:
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(contents.encode()))

        # The header is finished
        self.end_headers()

        # Send the response message
        self.wfile.write(contents.encode())

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
