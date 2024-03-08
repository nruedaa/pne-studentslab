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

seq_list = [Seq("ACT"), Seq("GATA"), Seq("CAGATA")]
print_seqs(seq_list)