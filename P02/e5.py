from Seq1 import Seq
from Client0 import Client
PRACTICE = 2
EXERCISE = 5
IP = "192.168.1.198"
PORT = 8081
def req_response_from_server(client, msg):
    print("Gene FRAT1: {}".format(msg), sep="")
    response = client.talk(msg)
    print(f"From Server: {response}")
def create_fragment(sequence):
    fragment = ""
    count = 0
    fragment_list = []
    for i in sequence:
        count += 1
        if count <= 10:
            fragment += i
        else:
            fragment_list.append(fragment)
    return fragment_list
print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")
c = Client(IP, PORT)
s = Seq()
s.seq_read_fasta("../sequences/FRAT1.txt")
m = str(s)
req_response_from_server(c, m)
list = create_fragment(m)
frag = 0
for f in list:
    frag += 1
    print(f"Fragment", frag, ":", f)


