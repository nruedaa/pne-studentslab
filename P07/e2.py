import http.client
import json

genes_list = ["FRAT1", "ADA", "FXN", "RNU6-269P", "MIR633", "TTTY4C", "RBMY2YP", "FGFR3", "KDR", "ANK2"]
genes_ids = {}
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

for g in genes_list:
    gene_id = get_gene_id(g)
    if gene_id:
        genes_ids[g] = gene_id
    else:
        print("No information obtained for the gene", g)

print("Dictionary of Genes!\n", "There are", len(genes_ids), "genes in the dictionary:")
for k,v in genes_ids.items():
    print(k, ": -->", v)
