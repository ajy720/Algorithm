if __name__ == "__main__":
    n, m = map(int, input().split())

    arr = [i+1 for i in range(n)]

    for _ in " " * m:
        i, j = map(lambda x: int(x) - 1, input().split())

        arr[i:j+1] = reversed(arr[i:j+1])

    print(*arr)
