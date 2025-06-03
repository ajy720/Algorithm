if __name__ == "__main__":
    n = int(input())

    e = []
    cur = ()

    for x in range(n):
        for y, value in enumerate(map(int, input().split())):
            if value == 2:
                cur = (x + y) % 2

            elif value == 1:
                e.append((x, y))

    e = [(x, y) for (x, y) in e if (x + y) % 2 == cur]

    print("Lena" if not e else "Kiriya")
