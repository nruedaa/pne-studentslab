from Seq1 import Seq
print("-----| Practice 1, Exercise 8 |-----")
null_sequence = Seq()
valid_sequence = Seq("ACTGA")
invalid_sequence = Seq("Invalid sequence")

print("Sequence 1:", "(Length: ", null_sequence.len(), ")", null_sequence)
print(" Bases:", null_sequence.seq_count(), end = ", ")
print("\n Rev:", null_sequence.seq_reverse())
print(" Comp:", null_sequence.seq_complement())

print("\nSequence 2:", "(Length: ", valid_sequence.len(), ")", valid_sequence)
print(" Bases:", valid_sequence.seq_count(), end = ", ")
print("\n Rev:", valid_sequence.seq_reverse())
print(" Comp:", valid_sequence.seq_complement())

print("\nSequence 3:", "(Length: ", invalid_sequence.len(), ")", invalid_sequence)
print(" Bases:", invalid_sequence.seq_count(), end = ", ")
print("\n Rev:", invalid_sequence.seq_reverse())
print(" Comp:", invalid_sequence.seq_complement())
