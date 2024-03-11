import socket
import termcolor
from Seq1 import Seq
class Server:
    def __init__(self):
        PORT = 8080
        IP = "127.0.0.1"
        MAX_OPEN_REQUESTS = 5
        number_con = 5
        serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        serversocket.bind((IP, PORT))
        serversocket.listen(MAX_OPEN_REQUESTS)
        print("SEQ server configured")
        while True:
            print("Waiting for clients...")
            try:
                (clientsocket, address) = serversocket.accept()
                number_con += 1
            except socket.error:
                print("Problems using ip {} port {}. Is the IP correct? Do you have port permission?".format(IP, PORT))
            except KeyboardInterrupt:
                print("Server stopped by the user")
                serversocket.close()
                exit()
            else:
                msg = clientsocket.recv(2048).decode("utf-8")
                message = self.execute_response(msg)
                response = message.encode()
                clientsocket.send(response)
                clientsocket.close()

    def execute_response(self, msg):
        if msg.startswith("PING"):
            return self.ping_response()
        elif msg.startswith("GET"):
            return self.get_response(msg)
        elif msg.startswith("INFO"):
            return self.info_response(msg)
        elif msg.startswith("COMP"):
            return self.complement_response(msg)
        elif msg.startswith("REV"):
            return self.reverse_response(msg)
        elif msg.startswith("GENE"):
            return self.gene_response(msg)
        else:
            return "Invalid command"
    def ping_response(self):
        termcolor.cprint("PING command", "green")
        print("OK!")
        return "OK\n"

    def get_response(self, msg):
        n = msg.replace("GET", "")
        termcolor.cprint("GET", "green")
        list_sequences = ["AAAACCCCGGGGTTTT", "CCCCGGGGTTTTAAAA", "ACGTACGTACGTACGTACGTACGT", "GTGTGTCACACAGTGTGTCACA", "AAACAAATAAAGGGGCGGGTGGGA"]
        user_sequence = list_sequences[int(n)]
        print(user_sequence + "\n")
        return user_sequence + "\n"

    def info_response(self, msg):
        sequence = ""
        for i in msg:
            if i in "ACGT":
                sequence += i
        termcolor.cprint("INFO", "green")
        s = Seq(sequence)
        bases_list = ["A", "C", "T", "G"]
        result = f"Sequence {s}\nTotal Length: {s.len()}\n"
        for j in bases_list:
            average = (round(s.seq_count_base(j) / s.len() * 100, 2))
            result += f"{j}: {s.seq_count_base(j)}  ({average}%)\n"
        print(result)
        return result

    def complement_response(self, msg):
        sequence = ""
        msg = msg.lstrip("COMP")
        for i in msg:
            if i in "ACGT":
                sequence += i
        termcolor.cprint("COMP", "green")
        s = Seq(sequence)
        comp_seq = s.seq_complement()
        print(comp_seq + "\n")
        return comp_seq + "\n"

    def reverse_response(self, msg):
        sequence = ""
        for i in msg:
            if i in "ACGT":
                sequence += i
        termcolor.cprint("REV", "green")
        s = Seq(sequence)
        rev_seq = s.seq_reverse()
        print(rev_seq + "\n")
        return rev_seq + "\n"

    def gene_response(self, msg):
        gene = msg.lstrip("GENE ")
        termcolor.cprint("GENE", "green")
        filename = "../sequences/" + gene + ".txt"
        s = Seq()
        sequence = s.seq_read_fasta(filename)
        print(sequence + "\n")
        return sequence + "\n"

c = Server()
