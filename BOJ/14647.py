if __name__ == "__main__":
    n, m = map(int, input().split())

    row = []
    col = [0] * m
    for _ in ' '*n:
        arr = input().split()
        s = 0

        for i in range(len(arr)):
            s += arr[i].count('9')
            col[i] += arr[i].count('9')

        row.append(s)

    print(sum(row) - max(max(row), max(col)))
