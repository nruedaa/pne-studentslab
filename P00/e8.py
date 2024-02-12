from Seq0 import *
folder = "../sequences/"
genes_list = ["U5.txt", "ADA.txt", "FRAT1.txt", "FXN.txt"]
bases_list = ["A", "C", "T", "G"]
for i in genes_list:
    count_bases = []
    for j in bases_list:
        count_bases.append(seq_count_base(folder + i, j))
    for b in count_bases:
        most_frequent = max(count_bases)
    print("Gene", i.replace(".txt", ""), ": Most frequent Base:", most_frequent)
