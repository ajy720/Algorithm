if __name__ == "__main__":
    n, m = map(int, input().split())

    arr = [i for i in range(n + 1)]

    for _ in " " * m:
        i, j = map(int, input().split())

        arr[i], arr[j] = arr[j], arr[i]

    print(*arr[1:])
