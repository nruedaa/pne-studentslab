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
                message = self.execute_response(str(msg)) + "\n"
                response = str.encode(message)
                clientsocket.send(response)
                clientsocket.close()

    def execute_response(self, msg, n = None, sequence = None, gene = None):
        if msg.startswith("PING"):
            return self.ping_response()
        elif msg.startswith("GET"):
            return self.get_response(n)
        elif msg.startswith("INFO"):
            return self.info_response(sequence)
        elif msg.startswith("COMP"):
            return self.complement_response(sequence)
        elif msg.startswith("REV"):
            return self.reverse_response(sequence)
        elif msg.startswith("GENE"):
            return self.gene_response(gene)
    def ping_response(self):
        termcolor.cprint("PING command", "green")
        print("OK!")
        return "OK\n"

    def get_response(self, n):
        termcolor.cprint("GET", "green")
        list_sequences = ["AAAACCCCGGGGTTTT", "CCCCGGGGTTTTAAAA", "ACGTACGTACGTACGTACGTACGT", "GTGTGTCACACAGTGTGTCACA", "AAACAAATAAAGGGGCGGGTGGGA"]
        user_sequence = list_sequences[n]
        print(user_sequence)
        return user_sequence

    def info_response(self, sequence):
        termcolor.cprint("INFO", "green")
        s = Seq(sequence)
        bases_list = ["A", "C", "T", "G"]
        print(" Sequence:", s, "\n", "Total Length:", s.len())
        for j in bases_list:
            average = (round(sequence.count(j) / s.len() * 100, 2))
            print(j, ":", s.seq_count_base(j), "(", average, "% )")
        return " Sequence:", s, "\n", "Total Length:", s.len()

    def complement_response(self, sequence):
        termcolor.cprint("COMP", "green")
        s = Seq(sequence)
        comp_seq = s.seq_complement()
        print(comp_seq)
        return comp_seq

    def reverse_response(self, sequence):
        termcolor.cprint("REV", "green")
        s = Seq(sequence)
        rev_seq = s.seq_reverse()
        print(rev_seq)
        return rev_seq

    def gene_response(self, gene):
        termcolor.cprint("GENE", "green")
        filename = "../sequences/" + gene + ".txt"
        s = Seq()
        sequence = s.seq_read_fasta(filename)
        print(sequence)
        return sequence

c = Server()
