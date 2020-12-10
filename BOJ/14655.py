if __name__ == "__main__":
    n = int(input())

    arr = [*map(lambda x: abs(int(x)), input().split())]
    arr2 = [*map(lambda x: abs(int(x)), input().split())]

    print(sum(arr + arr2))

