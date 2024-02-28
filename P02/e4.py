from Seq1 import Seq
from Client0 import Client
genes = ["U5.txt", "FRAT1.txt", "ADA.txt"]
folder = "../sequences/"
PRACTICE = 2
EXERCISE = 4
# -- Parameters of the server to talk to
IP = "212.128.255.104"  # your IP address
PORT = 8081
def get_file(gene):
    return folder + gene
def req_response_from_server(client, msg):
    print("To server: {}".format(msg), sep= "")
    response = client.talk(msg)
    print(f"From Server: {response}")
print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

# -- Create a client object
c = Client(IP, PORT)

for g in genes:
    s = Seq()
    s.seq_read_fasta(get_file(g))
    m = "Sending " + g + " Gene to the server..."
    req_response_from_server(c, m)
    m = str(s)
    req_response_from_server(c, m)
