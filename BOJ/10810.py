if __name__ == "__main__":
    n, m = map(int, input().split())

    arr = [0] * (n)

    for _ in " " * m:
        i, j, k = map(int, input().split())
        for idx in range(i, j + 1):
            arr[idx - 1] = k

    print(*arr)
