if __name__ == "__main__":
    n = int(input())

    arr = [300, 60, 10]

    ans = []
    for i in arr:
        ans.append(n // i)
        n %= i

    if n:
        print(-1)
    else:
        print(*ans)
