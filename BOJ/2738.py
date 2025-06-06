if __name__ == "__main__":
    n, m = map(int, input().split())

    arr1, arr2 = [], []

    for _ in " " * n:
        arr1.append([*map(int, input().split())])

    for _ in " " * n:
        arr2.append([*map(int, input().split())])

    for rowA, rowB in zip(arr1, arr2):
        print(*[a+ b for a, b in zip(rowA, rowB)])