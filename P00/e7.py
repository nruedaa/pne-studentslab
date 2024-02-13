from Seq0 import *
body = seq_read_fasta("../sequences/U5.txt")
fragment, complement = seq_complement(body, 20)
print("-----|Exercise 7|-----", "\n", "Gene U5:", "\n", "Frag:", fragment, "\n", "Comp:", complement)

