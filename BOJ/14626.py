bias = [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0], [0, 7, 4, 1, 8, 5, 2, 9, 6, 3, 0]]

if __name__ == "__main__":
    s = input()
    acc = 0
    pos = 0
    for idx, c in enumerate(s):
        if c == "*":
            pos = idx
        else:
            p = 3 if idx % 2 else 1
            acc += int(c) * (p)
    print(bias[1 if pos % 2 else 0][(10 - (acc % 10)) % 10])
