from Seq1 import Seq
print("-----| Practice 1, Exercise 5 |-----")
null_sequence = Seq()
valid_sequence = Seq("ACTGA")
invalid_sequence = Seq("Invalid sequence")
bases_list = ["A", "C", "T", "G"]
print("Sequence 1:", "(Length: ", null_sequence.len(), ")", null_sequence)
for i in bases_list:
    print(i, ":", null_sequence.seq_count_base(i), end = ", ")
print("\nSequence 2:", "(Length: ", valid_sequence.len(), ")", valid_sequence)
for i in bases_list:
    print(i, ":", valid_sequence.seq_count_base(i), end = ", ")

print("\nSequence 3:", "(Length: ", invalid_sequence.len(), ")", invalid_sequence)
for i in bases_list:
    print(i, ":", invalid_sequence.seq_count_base(i), end = ", ")