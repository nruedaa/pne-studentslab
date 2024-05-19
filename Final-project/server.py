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
    if "id" in response:
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
            print(length)
            names = []
            for i in species_list:
                names.append(i.get("display_name", "Unknown"))
            limit = (arguments.get("limit", [str(length)])[0])
            if limit.isdigit():
                limit = int(limit)
                contents = read_html_file("species.html").render(
                    context={"length": length, "limit": limit, "species": names})
                self.send_response(200)
            else:
                contents = Path('./html/error.html').read_text()
                self.send_response(404)
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
                if karyotype_list:
                    contents = read_html_file("karyotype.html").render(
                        context={"specie_name": specie, "chromosomes": karyotype_list})
                    self.send_response(200)
                else:
                    contents = Path('./html/error.html').read_text()
                    self.send_response(404)
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
                if "top_level_region" in response and response["top_level_region"]:
                    found = False
                    information = response["top_level_region"]
                    for t in information:
                        if t["name"] == chromosome_input:
                            if t["coord_system"] == "chromosome":
                                chromosome_length = t["length"]
                                contents = read_html_file("chromosome_length.html").render(
                                    context={"species_name": species_input.upper(), "chromosome_name": chromosome_input, "chromosome_length": chromosome_length})
                                self.send_response(200)
                                found = True
                    if not found:
                        contents = Path('./html/error.html').read_text()
                        self.send_response(404)
                else:
                    contents = Path('./html/error.html').read_text()
                    self.send_response(404)
            else:
                contents = Path('./html/error.html').read_text()
                self.send_response(404)
        elif path == "/geneSeq":
            gene_name = (arguments.get("gene", [""])[0]).upper()
            if gene_name:
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
                    if "seq" in response:
                        seq = response.get("seq", [])
                        contents = read_html_file("sequence.html").render(
                            context={"sequence": seq, "gene": gene_name})
                        self.send_response(200)
                else:
                    contents = Path('./html/error.html').read_text()
                    self.send_response(404)
            else:
                contents = Path('./html/error.html').read_text()
                self.send_response(404)
        elif path == "/geneInfo":
            gene_name = (arguments.get("gene", [""])[0]).upper()
            if gene_name:
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
                if "id" in response:
                    gene_id = response["id"]
                    start_point = response["start"]
                    end_point = response["end"]
                    chromosome_name = response["seq_region_name"]
                    gene_length = int(end_point) - int(start_point)
                    contents = read_html_file("information.html").render(
                        context={"gene": gene_name, "gene_id": gene_id, "start": start_point, "end": end_point, "chromosome": chromosome_name, "gene_length": gene_length})
                    self.send_response(200)
                else:
                    contents = Path('./html/error.html').read_text()
                    self.send_response(404)
            else:
                contents = Path('./html/error.html').read_text()
                self.send_response(404)
        elif path == "/geneCalc":
            gene_name = (arguments.get("gene", [""])[0]).upper()
            if gene_name:
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
                    self.send_response(404)
            else:
                contents = Path('./html/error.html').read_text()
                self.send_response(404)
        elif path == "/geneList":
            chromosome_name = (arguments.get("chromo", [""])[0]).upper()
            start_point = (arguments.get("start", [""])[0])
            end_point = (arguments.get("end", [""])[0])
            valid_human_chromo = []
            for i in range(1, 24):
                valid_human_chromo.append(str(i))
            valid_human_chromo.append("X")
            valid_human_chromo.append("Y")
            valid_human_chromo.append("MT")
            if start_point.isdigit() and end_point.isdigit() and int(start_point) < int(end_point) and (chromosome_name in valid_human_chromo):
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
                if response:
                    gene_id_list = []
                    for i in response:
                        if "gene_id" in i:
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
                            if "description" in response2:
                                gene_name_list.append(response2["description"])
                    contents = read_html_file("genes_list.html").render(
                        context={"chromosome_name": chromosome_name, "start": start_point, "end":end_point, "list_genes": gene_name_list})
                    self.send_response(200)
                else:
                    contents = Path('./html/error.html').read_text()
                    self.send_response(404)
            else:
                contents = Path('./html/error.html').read_text()
                self.send_response(404)
        else:
            contents = Path('./html/error.html').read_text()
            self.send_response(404)
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(str.encode(contents)))
        self.end_headers()
        self.wfile.write(str.encode(contents))
        return
Handler = TestHandler
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Serving at PORT", PORT)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stopped by the user")
        httpd.server_close()
