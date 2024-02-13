from Seq0 import *
folder = "../sequences/"
genes_list = ["U5.txt", "ADA.txt", "FRAT1.txt", "FXN.txt"]
print("-----| Exercise 5|-----")
for i in genes_list:
    body = seq_read_fasta(folder + i)
    print("Gene", i.replace(".txt", ""), ":", seq_count(body))

