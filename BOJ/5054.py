if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input())
        arr = sorted(map(int, input().split()))

        print((arr[-1] - arr[0]) * 2)
