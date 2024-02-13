from Seq0 import *

body = seq_read_fasta("../sequences/U5.txt")
fragment, reverse = seq_reverse(body, 20)
print("-----|Exercise 6|-----", "\n", "Gene U5", "\n", "Fragment:", fragment, "\n", "Reverse:", reverse)
