def seq_ping():
    print("OK")

def seq_read_fasta(filename):
    from pathlib import Path
    first_line = Path(filename).read_text().find("\n")
    body = Path(filename).read_text()[first_line:]
    body = body.replace("\n", "")
    return body
def seq_len(filename):
    body = seq_read_fasta(filename)
    return len(body)
def seq_count_base(filename, base):
    body = seq_read_fasta(filename)
    count_base = body.count(base)
    return count_base
def seq_count(filename):
    body = seq_read_fasta(filename)
    bases_dictionary = {"A": 0,
                        "C": 0,
                        "G": 0,
                        "T": 0}
    for i in body:
      if i in bases_dictionary:
          bases_dictionary[i] += 1
    return bases_dictionary
def seq_reverse(filename, n):
    body = seq_read_fasta(filename)
    fragment = body[0:n]
    reverse = ""
    for i in reversed(fragment):
        reverse += i
    return fragment, reverse

def seq_complement(filename, n):
    body = seq_read_fasta(filename)
    fragment = body[0:n]
    complement = ""
    for i in fragment:
        if i == "A":
            complement += "T"
        elif i == "T":
            complement += "A"
        elif i == "C":
            complement += "G"
        elif i == "G":
            complement += "C"
    return fragment, complement