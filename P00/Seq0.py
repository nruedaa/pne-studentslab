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
    bases_dictionary = {"A:", 0, "T:", 0, "C:", 0, "G:", 0}
    for i in body:
        bases_dictionary[i] += 1



