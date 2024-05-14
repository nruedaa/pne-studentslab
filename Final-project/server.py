import http.server
import socketserver
import termcolor
from pathlib import Path
from urllib.parse import parse_qs, urlparse
import jinja2 as j
import http.client
import json
PORT = 8080
socketserver.TCPServer.allow_reuse_address = True
def read_html_file(filename):
    contents = Path("html/" + filename).read_text()
    contents = j.Template(contents)
    return contents

def get_gene_id(gene):
    SERVER = "rest.ensembl.org"
    PATH = f"/lookup/symbol/human/{gene}?content-type=application/json"
    conn = http.client.HTTPConnection(SERVER)
    try:
        conn.request("GET", PATH)

    except ConnectionRefusedError:
        print("ERROR! Cannot connect to the Server")
        exit()
    r1 = conn.getresponse()
    data1 = r1.read().decode("utf-8")
    response = json.loads(data1)
    gene_id = response["id"]
    return gene_id

class TestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        url_path = urlparse(self.path)
        path = url_path.path
        arguments = parse_qs(url_path.query)
        termcolor.cprint(self.requestline, 'green')
        if path == "/" or path.startswith("/echo"):
            contents = Path('./html/index.html').read_text()
            self.send_response(200)
        elif path == "/listSpecies":
            limit = int(arguments.get("limit", [""])[0])
            SERVER = "rest.ensembl.org"
            ENDPOINT = "/info/species"
            PARAMS = "?content-type=application/json"
            conn = http.client.HTTPConnection(SERVER)
            try:
                conn.request("GET", ENDPOINT + PARAMS)
            except ConnectionRefusedError:
                print("ERROR! Cannot connect to the Server")
                exit()
            r1 = conn.getresponse()
            print(f"Response received!: {r1.status} {r1.reason}\n")
            data1 = r1.read().decode("utf-8")
            response = json.loads(data1)
            species_list = response["species"]
            length = len(species_list)
            names = []
            for i in species_list:
                names.append(i["display_name"])
            contents = read_html_file("species.html").render(
                context={"length": length, "limit": limit, "species": names})
            self.send_response(200)
        elif path == "/karyotype":
            species_input = arguments.get("species", [""])[0]
            SERVER = "rest.ensembl.org"
            ENDPOINT = f"/info/assembly/{species_input}"
            PARAMS = "?content-type=application/json"
            conn = http.client.HTTPConnection(SERVER)
            try:
                conn.request("GET", ENDPOINT + PARAMS)
            except ConnectionRefusedError:
                print("ERROR! Cannot connect to the Server")
                exit()
            r1 = conn.getresponse()
            print(f"Response received!: {r1.status} {r1.reason}\n")
            data1 = r1.read().decode("utf-8")
            response = json.loads(data1)
            karyotipe_list = response["karyotype"]
            contents = read_html_file("karyotype.html").render(
                context={"chromosomes": karyotipe_list})
            self.send_response(200)
        elif path == "/chromosomeLength":
            species_input = arguments.get("species", [""])[0]
            chromosome_input = arguments.get("chromosome", [""])[0]
            SERVER = "rest.ensembl.org"
            ENDPOINT = f"/info/assembly/{species_input}"
            PARAMS = "?content-type=application/json"
            conn = http.client.HTTPConnection(SERVER)
            try:
                conn.request("GET", ENDPOINT + PARAMS)
            except ConnectionRefusedError:
                print("ERROR! Cannot connect to the Server")
                exit()
            r1 = conn.getresponse()
            print(f"Response received!: {r1.status} {r1.reason}\n")
            data1 = r1.read().decode("utf-8")
            response = json.loads(data1)
            for t in response["top_level_region"]:
                if t["coord_system"] == "chromosome":
                    if t["name"] == chromosome_input:
                        chromosome_length = t["length"]
                        print(chromosome_length)
                        contents = read_html_file("chromosome_length.html").render(
                            context={"chromosome_length": chromosome_length})
            self.send_response(200)
        elif path == "/geneSeq":
            gene_name = (arguments.get("gene", [""])[0]).upper()
            SERVER = "rest.ensembl.org"
            ENDPOINT = "/sequence/id/"
            id = get_gene_id(gene_name)
            PARAMS = "?content-type=application/json"
            conn = http.client.HTTPConnection(SERVER)
            if id:
                try:
                    conn.request("GET", ENDPOINT + id + PARAMS)
                except ConnectionRefusedError:
                    print("ERROR! Cannot connect to the Server")
                    exit()

                r1 = conn.getresponse()
                print(f"Response received!: {r1.status} {r1.reason}\n")

                data1 = r1.read().decode("utf-8")
                response = json.loads(data1)
                seq = response["seq"]
                contents = read_html_file("sequence.html").render(
                    context={"sequence": seq, "gene": gene_name})
                self.send_response(200)
            else:
                contents = Path('./html/error.html').read_text()
                # Generating the response message
                self.send_response(404)
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
