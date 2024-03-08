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


s1 = Seq("ACCTGC")
s2 = Seq("Hello? Am I a valid sequence?")
print(f"Sequence 1: {s1}")
print(f"Sequence 2: {s2}")
