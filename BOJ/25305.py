if __name__ == "__main__":
    n, k = map(int, input().split())

    print(sorted(map(int, input().split()))[-k])
