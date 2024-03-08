list = ["AAAAAAAAAA", "CCCCCCCCCC", "GGGGGGGGG", "CCCCCCCCCCC"]
for f in range(4):
    message = f"Fragment {f + 1}: {list[f]}"
    if f // 2 == 0:
        print(list[f])

