def seq_ping():
    print("OK")

def seq_read_fasta(filename):
    from pathlib import Path
    first_line = Path(filename).read_text().find("\n")
    body = Path(filename).read_text()[first_line:]
    body = body.replace("\n", "")
    return body
def seq_len(body):
    length = len(body)
    return length
def seq_count_base(body, base):
    count_base = body.count(base)
    return count_base
def seq_count(body):
    bases_dictionary = {"A": 0,
                        "C": 0,
                        "G": 0,
                        "T": 0}
    for i in body:
      if i in bases_dictionary:
          bases_dictionary[i] += 1
    return bases_dictionary
def seq_reverse(body, n):
    fragment = body[0:n]
    reverse = ""
    for i in reversed(fragment):
        reverse += i
    return fragment, reverse

def seq_complement(body, n):
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

def most_frequent(body):
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

