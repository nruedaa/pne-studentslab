from Seq1 import Seq
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
genes_list = ["FRAT1", "ADA", "FXN", "RNU6-269P", "MIR633", "TTTY4C", "RBMY2YP", "FGFR3", "KDR", "ANK2"]
gene_name = input("Enter gene name:").upper()
if gene_name in genes_list:
    SERVER = "rest.ensembl.org"
    ENDPOINT = "/sequence/id/"
    GENE_ID = get_gene_id(gene_name)
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
    bases_list = ["A", "C", "T", "G"]
    print("Gene:", gene_name)
    print("Description:", description)
    seq_calculations = Seq(sequence)
    print("Total length:", seq_calculations.len())
    for i in bases_list:
        average = seq_calculations.seq_count_base(i)*100/seq_calculations.len()
        print(i, ":", seq_calculations.seq_count_base(i), "(", round(average, 1) , "%)")
    print("Most frequent Base:", seq_calculations.most_frequent())
else:
    print("Gene could not be identified.")