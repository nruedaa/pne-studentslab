from Seq0 import *
folder = "../sequences/"
genes_list = ["U5.txt", "ADA.txt", "FRAT1.txt", "FXN.txt"]
for i in genes_list:
    length = seq_len(folder + i)
    print("Gene " + i.replace(".txt", "") + "-> Length:", length)



