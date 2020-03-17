if __name__ == "__main__":
    n = int(input())

    arr = set([*map(int, input().split())])

    m = int(input())

    chk_arr = [*map(int, input().split())]

    for i in chk_arr:
        if i in arr:
            print(1)
        else:
            print(0)