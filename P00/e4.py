from Seq0 import *
folder = "../sequences/"
genes_list = ["U5.txt", "ADA.txt", "FRAT1.txt", "FXN.txt"]
bases_list = ["A", "C", "T", "G"]
for i in genes_list:
    print("Gene", i.replace(".txt", ""), ":")
    for j in bases_list:
        print(j, seq_count_base(folder + i, j))

