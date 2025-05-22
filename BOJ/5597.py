if __name__ == "__main__":
    arr = [i + 1 for i in range(30)]
    for _ in " " * 28:
        n = int(input())
        arr.remove(n)

    arr.sort()

    print(*arr, sep="\n")
