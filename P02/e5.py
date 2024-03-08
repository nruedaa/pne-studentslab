from Seq1 import Seq
from Client0 import Client
PRACTICE = 2
EXERCISE = 5
IP = "212.128.255.39"
PORT = 8080
def req_response_from_server(client, msg, sender = "Server"):
    if sender == "Server":
        print("{}".format(msg), sep="")
    response = client.talk(msg)
def create_fragment(sequence):
    fragment = ""
    count = 0
    fragment_list = []
    for i in sequence:
        count += 1
        fragment += i
        if count == 10:
            fragment_list.append(fragment)
            fragment = ""
            count = 0
    if fragment:
        fragment_list.append(fragment)

    fragment_list.append(fragment)
    return fragment_list
print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")
c = Client(IP, PORT)
s = Seq()
s.seq_read_fasta("../sequences/FRAT1.txt")
m = str(s)
print("Gene FRAT1 {}".format(m), sep="")
sending = "Sending FRAT1 Gene to the server in fragments of 10 bases"
req_response_from_server(c, sending, "Client")
list = create_fragment(m)
for f in range(5):
    message = f"Fragment {f + 1}: {list[f]}"
    req_response_from_server(c, message)


