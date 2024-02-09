count = 0
count_a = 0
count_c = 0
count_g = 0
count_t = 0

with open("dna.txt", "r") as f:
    for i in f:
        for j in i:
            if j == "A" or j == "C" or j == "G" or j =="T":
                count += 1
                if j == "A":
                    count_a += 1
                elif j == "C":
                    count_c += 1
                elif j == "G":
                    count_g += 1
                elif j == "T":
                    count_t += 1
print("Total number of bases:", count, "\n", "Number of A:", count_a, "\n", "Number of C:", count_c, "\n", "Number of G:", count_g, "\n", "Number of T:", count_t)
