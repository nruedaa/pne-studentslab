from Seq0 import *
folder = "../sequences/"
genes_list = ["U5.txt", "ADA.txt", "FRAT1.txt", "FXN.txt"]
bases_list = ["A", "C", "T", "G"]
print("-----| Exercise 5|-----")
for i in genes_list:
    print("Gene", i.replace(".txt", ""), ":", seq_count(folder + i))
