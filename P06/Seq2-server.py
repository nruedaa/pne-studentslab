import http.server
import socketserver
import termcolor
from pathlib import Path
from urllib.parse import parse_qs, urlparse
import jinja2 as j

PORT = 8080
def read_html_file(filename):
    contents = Path("html/" + filename).read_text()
    contents = j.Template(contents)
    return contents
def get_response(n):
    list_sequences = ["AAAACCCCGGGGTTTT", "CCCCGGGGTTTTAAAA", "ACGTACGTACGTACGTACGTACGT", "GTGTGTCACACAGTGTGTCACA", "AAACAAATAAAGGGGCGGGTGGGA"]
    user_sequence = list_sequences[int(n)]
    print(user_sequence + "\n")
    return user_sequence + "\n"
def seq_read_fasta(filename):
    from pathlib import Path
    first_line = Path(filename).read_text().find("\n")
    body = Path(filename).read_text()[first_line:]
    body = body.replace("\n", "")
    return body

sequence_1 = seq_read_fasta("../sequences/U5.txt")
sequence_2 = seq_read_fasta("../sequences/ADA.txt")
sequence_3 = seq_read_fasta("../sequences/FRAT1.txt")
sequence_4 = seq_read_fasta("../sequences/FXN.txt")

socketserver.TCPServer.allow_reuse_address = True

class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        url_path = urlparse(self.path)
        path = url_path.path
        arguments = parse_qs(url_path.query)
        termcolor.cprint(self.requestline, 'green')
        if path == "/" or path.startswith("/echo"):
            contents = Path('./html/index.html').read_text()
            self.send_response(200)
        elif path == "/ping":
            contents = Path('./html/ping.html').read_text()
            self.send_response(200)
        elif path == "/get":
            number = arguments.get("sequence", [""])[0]
            sequence = get_response(number)
            contents = read_html_file("get.html").render(
                context={"number": number, "sequence": sequence})
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
