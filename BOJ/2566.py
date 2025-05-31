if __name__ == "__main__":
    x, y = 0, 0
    n = 0

    for i in range(9):
        row = [*map(int, input().split())]
        max_r = max(row)

        if n < max_r:
            x = i
            y = row.index(max_r)
            n = max_r

    print(n)
    print(x + 1, y + 1)
