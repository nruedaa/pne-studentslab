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
    return body

def seq_reverse(body):
    reverse = ""
    for i in reversed(body):
        reverse += i
    return reverse

def seq_complement(body):
    complement = ""
    for i in body:
        if i == "A":
            complement += "T"
        elif i == "T":
            complement += "A"
        elif i == "C":
            complement += "G"
        elif i == "G":
            complement += "C"
    return complement

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
            number = arguments.get("number", [""])[0]
            sequence = get_response(number)
            contents = read_html_file("get.html").render(
                context={"number": number, "sequence": sequence})
            self.send_response(200)
        elif path == "/gene":
            gene = arguments.get("gene", [""])[0]
            gene_seq = seq_read_fasta("../sequences/" + gene + ".txt")
            contents = read_html_file("gene.html").render(
                context={"gene": gene, "gene_seq": gene_seq})
            self.send_response(200)
        elif path == "/operation":
            introduced_seq = arguments.get("msg", [""])[0].upper()
            operation = arguments.get("op", [""])[0]
            if operation == "Rev":
                seq_reversed = seq_reverse(introduced_seq)
                contents = read_html_file("operation.html").render(
                    context={"introduced_seq": introduced_seq, "operation": operation, "result": seq_reversed})
                self.send_response(200)
            elif operation == "Comp":
                complement = seq_complement(introduced_seq)
                contents = read_html_file("operation.html").render(
                    context={"introduced_seq": introduced_seq, "operation": operation, "result": complement})
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
