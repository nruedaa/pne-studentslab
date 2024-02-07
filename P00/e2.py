from Seq0 import *
FOLDER = "../sequences/"
FILENAME = "U5.txt"
print("DNA FILE:", FILENAME)
body = seq_read_fasta("../sequences/U5.txt")
print("The first 20 bases are:", body[0:20])
