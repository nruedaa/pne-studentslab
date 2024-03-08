class Seq:
    def __init__(self, strbases = None):
        self.strbases = strbases
        correct_bases = ["A", "C", "G", "T"]
        result = True
        if self.strbases == None:
            print("NULL sequence created")
            self.strbases = "NULL"
        else:
            for i in self.strbases:
                if i not in correct_bases:
                    result = False
            if result:
                print("New sequence created!")
            else:
                self.strbases = "ERROR"
                print("INVALID sequence!")


    def __str__(self):
        return self.strbases
    def len(self):
        """Calculate the length of the sequence"""
        if self.strbases == "NULL" or self.strbases == "ERROR":
            length = 0
        else:
            length = len(self.strbases)
        return length

    def seq_count_base(self, base):
        if self.strbases == "NULL"or self.strbases == "ERROR":
            count_base = 0
        else:
            for i in self.strbases:
                if i == base:
                    count_base = self.strbases.count(base)
        return count_base

    def seq_count(self):
        bases_dictionary = {"A": 0,
                            "C": 0,
                            "G": 0,
                            "T": 0}
        if self.strbases == "NULL" or self.strbases == "ERROR":
            bases_dictionary = {"A": 0,
                                "C": 0,
                                "G": 0,
                                "T": 0}
        else:
            for i in self.strbases:
                if i in bases_dictionary:
                    bases_dictionary[i] += 1
        return bases_dictionary

    def seq_reverse(self):
        reverse = ""
        if self.strbases == "NULL":
            reverse = "NULL"
        elif self.strbases == "ERROR":
            reverse = "ERROR"
        else:
            for i in reversed(self.strbases):
                reverse += i
        return reverse

    def seq_complement(self):
        complement = ""
        if self.strbases == "NULL":
            complement = "NULL"
        elif self.strbases == "ERROR":
            complement = "ERROR"
        else:
            for i in self.strbases:
                if i == "A":
                    complement += "T"
                elif i == "T":
                    complement += "A"
                elif i == "C":
                    complement += "G"
                elif i == "G":
                    complement += "C"
        return complement

    def seq_read_fasta(self, filename):
        from pathlib import Path
        first_line = Path(filename).read_text().find("\n")
        body = Path(filename).read_text()[first_line:]
        body = body.replace("\n", "")
        self.strbases = body
        return body

    def most_frequent(self):
        body = self.strbases
        a = body.count("A")
        c = body.count("C")
        g = body.count("G")
        t = body.count("T")
        max_base = max(a, c, g, t)
        if max_base == a:
            freq = "A"
        elif max_base == c:
            freq = "C"
        elif max_base == g:
            freq = "G"
        elif max_base == t:
            freq = "T"
        return freq