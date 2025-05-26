if __name__ == "__main__":

    n = int(input())
    arr = [*map(int, input().split())]
    arr2 = sorted(set(arr))

    d = {value: idx for idx, value in enumerate(arr2)}

    print(*[d[el] for el in arr])
