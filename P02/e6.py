def create_fragment(sequence):
    fragment = ""
    count = 0
    fragment_list = []
    for i in sequence:
        count += 1
        if count <= 10:
            fragment += i
        else:
            fragment_list.append(fragment)
    return fragment_list
fragment_list = create_fragment("ACGTACGTACGTTTTTT")
print(fragment_list)
fragment = 0
for f in fragment_list:
    fragment += 1
    print(f"Fragment:", fragment, f)


