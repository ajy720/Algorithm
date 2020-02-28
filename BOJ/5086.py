while 1:
    a, b = map(int, input().split())
    if a+b == 0: exit()

    if max(a, b) % min(a, b) == 0:
        print("multiple" if a > b else "factor")
    else:
        print("neither")