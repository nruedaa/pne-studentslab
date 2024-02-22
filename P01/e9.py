from Seq1 import Seq
print("-----| Practice 1, Exercise 9 |-----")
s = Seq()
sequence = s.seq_read_fasta("../sequences/U5.txt")
seq = Seq(sequence)
print("Sequence 1:", "(Length: ", seq.len(), ")", seq)
print(" Bases:", seq.seq_count(), end = ", ")
print("\n Rev:", seq.seq_reverse())
print(" Comp:", seq.seq_complement())