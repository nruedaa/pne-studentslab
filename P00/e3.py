from Seq0 import *

folder = "../sequences/"
genes_list = ["U5.txt", "ADA.txt", "FRAT1.txt", "FXN.txt"]
for i in genes_list:
    body = seq_read_fasta(folder + i)
    length = seq_len(body)
    print("Gene " + i.replace(".txt", "") + "-> Length:", length)



