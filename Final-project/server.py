import http.server
import socketserver
import termcolor
from pathlib import Path
from urllib.parse import parse_qs, urlparse
import jinja2 as j
import http.client
import urllib.parse
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
            species_list = response.get("species", [])
            length = len(species_list)
            names = []
            for i in species_list:
                names.append(i.get("display_name", "Unknown"))
            limit = int(arguments.get("limit", [length])[0])
            contents = read_html_file("species.html").render(
                context={"length": length, "limit": limit, "species": names})
            self.send_response(200)
        elif path == "/karyotype":
            specie = arguments.get("species", [""])[0].replace("+", "").strip()
            species_input = urllib.parse.quote(specie)
            if species_input:
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
                karyotype_list = response.get("karyotype", [])
                contents = read_html_file("karyotype.html").render(
                    context={"chromosomes": karyotype_list})
                self.send_response(200)
            else:
                contents = Path('./html/error.html').read_text()
                self.send_response(404)
        elif path == "/chromosomeLength":
            species_input = arguments.get("species", [""])[0]
            chromosome_input = arguments.get("chromo", [""])[0]
            if species_input and chromosome_input:
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
                                context={"species_name": species_input.upper(), "chromosome_name": chromosome_input, "chromosome_length": chromosome_length})
                            self.send_response(200)
            else:
                contents = Path('./html/error.html').read_text()
                self.send_response(404)
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
                seq = response.get("seq", [])
                contents = read_html_file("sequence.html").render(
                    context={"sequence": seq, "gene": gene_name})
                self.send_response(200)
            else:
                contents = Path('./html/error.html').read_text()
                # Generating the response message
                self.send_response(404)
        elif path == "/geneInfo":
            gene_name = (arguments.get("gene", [""])[0]).upper()
            SERVER = "rest.ensembl.org"
            ENDPOINT = f"/lookup/symbol/human/{gene_name}"
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
            gene_id = response["id"]
            start_point = response["start"]
            end_point = response["end"]
            chromosome_name = response["seq_region_name"]
            gene_length = int(end_point) - int(start_point)
            contents = read_html_file("information.html").render(
                context={"gene": gene_name, "gene_id": gene_id, "start": start_point, "end": end_point, "chromosome": chromosome_name, "gene_length": gene_length})
            self.send_response(200)
        elif path == "/geneCalc":
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
                sequence_length = len(seq)
                a_count = round(seq.count("A")/sequence_length, 2)
                c_count = round(seq.count("C")/sequence_length, 2)
                g_count = round(seq.count("G")/sequence_length, 2)
                t_count = round(seq.count("T")/sequence_length, 2)
                contents = read_html_file("bases_average.html").render(
                    context={"gene": gene_name, "seq_length": sequence_length, "A": a_count, "C": c_count, "G": g_count, "T": t_count})
                self.send_response(200)
            else:
                contents = Path('./html/error.html').read_text()
                # Generating the response message
                self.send_response(404)
        elif path == "/geneList":
            chromosome_name = (arguments.get("chromo", [""])[0]).upper()
            start_point = (arguments.get("start", [""])[0])
            end_point = (arguments.get("end", [""])[0])
            SERVER = "rest.ensembl.org"
            ENDPOINT = f"/overlap/region/human/{chromosome_name}:{start_point}-{end_point}"
            PARAMS = "?feature=gene&content-type=application/json"
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
            gene_id_list = []
            for i in response:
                gene_id_list.append(i["gene_id"])
            gene_name_list = []
            for j in gene_id_list:
                endpoint_find_gene = f"/lookup/id/{j}"
                parameters = "?content-type=application/json"
                conn2 = http.client.HTTPConnection(SERVER)
                try:
                    conn2.request("GET", endpoint_find_gene + parameters)
                except ConnectionRefusedError:
                    print("ERROR! Cannot connect to the Server")
                    exit()
                r2 = conn2.getresponse()
                print(f"Response received!: {r2.status} {r2.reason}\n")
                data2 = r2.read().decode("utf-8")
                response2 = json.loads(data2)
                if "display_name" in response2:
                    gene_name_list.append(response2["display_name"])
                else:
                    if response2["description"]:
                        gene_name_list.append(response2["description"])
            contents = read_html_file("genes_list.html").render(
                context={"chromosome_name": chromosome_name, "start": start_point, "end":end_point, "list_genes": gene_name_list})
            self.send_response(200)
        else:
            contents = Path('./html/error.html').read_text()
            self.send_response(404)

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
