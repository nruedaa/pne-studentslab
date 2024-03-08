class Seq:
    def __init__(self, strbases):
        self.strbases = strbases
        correct_bases = ["A", "C", "G", "T"]
        for i in self.strbases:
            if i not in correct_bases:
                self.strbases = "ERROR"
        if self.strbases == "ERROR":
            print("INCORRECT sequence detected")
        else:
            print("New sequence created!")
    def __str__(self):
        """Method called when the object is being printed"""
        # -- We just return the string with the sequence
        return self.strbases
    def len(self):
        """Calculate the length of the sequence"""
        return len(self.strbases)
def print_seqs(seq_list):
    for index, i in enumerate(seq_list):
        length = i.len()
        sequence = i
        print("Sequence", index, ": (Length:", length, ") ", sequence)

def generate_seqs(pattern, number):
    new_seq_list = []
    for i in range(1, number + 1):
        new_seq_list.append(Seq(pattern * i))
    return new_seq_list
seq_list1 = generate_seqs("A", 3)
seq_list2 = generate_seqs("AC", 5)

print("List 1:")
print_seqs(seq_list1)

print()
print("List 2:")
print_seqs(seq_list2)
