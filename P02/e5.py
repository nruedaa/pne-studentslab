from Seq1 import Seq
from Client0 import Client

PRACTICE = 2
EXERCISE = 5
# -- Parameters of the server to talk to
IP = "212.128.255.139"  # your IP address
PORT = 8080

def req_response_from_server(client, msg):
    print("Gene FRAT1: {}".format(msg), sep="")
    response = client.talk(msg)
print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

# -- Create a client object
c = Client(IP, PORT)

s = Seq()
s.seq_read_fasta("../sequences/FRAT1.txt")
m = str(s)
req_response_from_server(c, m)
frag1 = m[0:10]
frag2 = m[10:20]
frag3 = m[20:30]
frag4 = m[30:40]
frag5 = m[40:50]
fragment_list = [frag1, frag2, frag3, frag4, frag5]
for i in fragment_list:
    req_response_from_server(c, i)
