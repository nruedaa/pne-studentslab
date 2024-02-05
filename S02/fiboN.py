
terms = int(input("Number of terms:"))
terms_list = [0]
variable1 = 0
variable2 = 1
while terms > 0:
    variable3 = variable1 + variable2
    variable1 = variable2
    variable2 = variable3
    terms_list.append(variable1)
    terms = terms - 1
print("5th fibonacci term: ", terms_list[5])
print("10th fibonacci term: ", terms_list[10])
print("15th fibonacci term: ", terms_list[15])

