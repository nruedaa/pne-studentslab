import http.client
import json
def get_gene_id(gene):
    SERVER = "rest.ensembl.org"
    PATH = f"/lookup/symbol/human/{gene}?content-type=application/json"
    conn = http.client.HTTPConnection(SERVER)
    try:
        conn.request("GET", PATH)
        r1 = conn.getresponse()
        data1 = r1.read().decode("utf-8")
        response = json.loads(data1)
        gene_id = response["id"]
    except ConnectionRefusedError:
        print("ERROR! Cannot connect to the Server")
        exit()
    return gene_id

SERVER = "rest.ensembl.org"
ENDPOINT = "/sequence/id/"
GENE_ID = get_gene_id("MIR633")
PARAMS = "?content-type=application/json"
URL = SERVER + ENDPOINT + GENE_ID + PARAMS
print(f"Server:{SERVER}")
print(f"URL:{URL}")

conn = http.client.HTTPConnection(SERVER)

try:
    conn.request("GET", ENDPOINT + GENE_ID + PARAMS)
except ConnectionRefusedError:
    print("ERROR! Cannot connect to the Server")
    exit()

r1 = conn.getresponse()
print(f"Response received!: {r1.status} {r1.reason}\n")

data1 = r1.read().decode("utf-8")
response = json.loads(data1)
description = response["desc"]
sequence = response["seq"]
print("Gene:", "MIR633")
print("Description:", description)
print("Bases:", sequence)
