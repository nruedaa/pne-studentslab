import http.server
import socketserver
import termcolor
from pathlib import Path
from urllib.parse import parse_qs, urlparse
import jinja2 as j

# Define the Server's port
PORT = 8080
def read_html_file(filename):
    contents = Path("html/" + filename).read_text()
    contents = j.Template(contents)
    return contents

# -- This is for preventing the error: "Port already in use"
socketserver.TCPServer.allow_reuse_address = True


# Class with our Handler. It is a called derived from BaseHTTPRequestHandler
# It means that our class inherits all his methods and properties
class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        """This method is called whenever the client invokes the GET method
        in the HTTP protocol request"""

        # Print the request line
        termcolor.cprint(self.requestline, 'green')

        # Open the form1.html file
        # Read the index from the file
        if self.path == "/" or self.path.startswith("/echo"):
            contents = Path('./html/form-e2.html').read_text()
            # Generating the response message
            self.send_response(200)  # -- Status line: OK!
            url_path = urlparse(self.path)
            path = url_path.path
            arguments = parse_qs(url_path.query)
            message = arguments.get("msg", [""])[0]
            check = arguments.get("chk", [""])[0]
            if message:
                if check:
                    message = message.upper()
                else:
                    message = message.lower()
                contents = read_html_file("response2.html").render(
                    context={"message": message})
                self.send_response(200)

            else:
                contents = Path("./html/form-e2.html").read_text()
                self.send_response(200)
        else:
            contents = Path('./html/error.html').read_text()
            # Generating the response message
            self.send_response(404)

        # Define the content-type header:
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(str.encode(contents)))

        # The header is finished
        self.end_headers()

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
