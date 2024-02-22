from Seq1 import Seq
print("-----| Practice 1, Exercise 4 |-----")
null_sequence = Seq()
valid_sequence = Seq("ACTGA")
invalid_sequence = Seq("Invalid sequence")
print("Sequence 1:", "(Length: ", null_sequence.len(), ")", null_sequence, "\nSequence 2:", "(Length: ", valid_sequence.len(), ")", valid_sequence, "\nSequence 3:", "(Length: ", invalid_sequence.len(), ")", invalid_sequence)
