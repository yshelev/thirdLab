for i in range(1, 1001):
    if i % 25 == 1:
        print("[", end="")

    if i % 25 == 0:
        print(i, end="]")
        print()
    else:
        print(i, end=", ")