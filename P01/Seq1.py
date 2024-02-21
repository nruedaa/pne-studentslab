class Seq:
    def __init__(self, strbases = None):
        correct_bases = ["A", "C", "G", "T"]
        if strbases == None:
            print("NULL sequence created")
            self.strbases = "NULL"
        else:
            for i in strbases:
                if i not in correct_bases:
                    self.strbases = "ERROR"
                    print("INVALID sequence!")
                else:
                    print("New sequence created!")
                    self.strbases = strbases
    def __str__(self):
        return self.strbases
    def len(self):
        """Calculate the length of the sequence"""
        if self.strbases == "NULL" or self.strbases == "ERROR":
            length = 0
        else:
            length = len(self.strbases)
        return length

