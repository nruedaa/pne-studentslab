from Seq1 import Seq
from Client0 import Client
PRACTICE = 2
EXERCISE = 5
IP = "212.128.255.39"
PORT1 = 8080
PORT2 = 8081
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
c1 = Client(IP, PORT1)
c2 = Client(IP, PORT2)
s = Seq()
s.seq_read_fasta("../sequences/FRAT1.txt")
m = str(s)
print("Gene FRAT1 {}".format(m), sep="")
sending = "Sending FRAT1 Gene to the server in fragments of 10 bases"
req_response_from_server(c1, sending, "Client")
req_response_from_server(c2, sending, "Client")
list = create_fragment(m)
for i, f in enumerate(list[0:10]):
    if (i + 1) % 2 == 0:
        message = f"Fragment {i + 1}: {list[i]}"
        req_response_from_server(c2, message)
    else:
        message = f"Fragment {i + 1}: {list[i]}"
        req_response_from_server(c1, message)



