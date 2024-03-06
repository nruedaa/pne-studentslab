from Seq1 import Seq
print("-----| Practice 1, Exercise 10 |-----")
folder = "../sequences/"
genes_list = ["U5.txt", "ADA.txt", "FRAT1.txt", "FXN.txt", "RNU6_269P.txt"]
bases_list = ["A", "C", "T", "G"]
for i in genes_list:
    count_bases = []
    s = Seq()
    body = s.seq_read_fasta(folder + i)
    seq = Seq(body)
    for j in bases_list:
        count_bases.append(seq.seq_count_base(j))
    print("Gene", i.replace(".txt", ""), ": Most frequent Base:", seq.most_frequent())
