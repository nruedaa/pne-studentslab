dna_seq = input("Introduce the sequence:").upper()
count_a = 0
count_c = 0
count_g = 0
count_t = 0

for i in dna_seq:
    if i == "A":
        count_a += 1
    elif i == "C":
        count_c += 1
    elif i == "G":
        count_g += 1
    elif i == "T":
        count_t += 1
print("Total length:", len(dna_seq))
print("\n", "A:", count_a, "\n", "C:", count_c, "\n", "T:", count_t, "\n", "G:", count_g)
