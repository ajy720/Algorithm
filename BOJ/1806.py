MAX_N = 100001

if __name__ == "__main__":
    n, bias = map(int, input().split())

    arr = [*map(int, input().split())]

    dp = [0] * n
    dp[0] = arr[0]
    for i in range(1, n):  # O(n)
        dp[i] = dp[i - 1] + arr[i]

    ans = MAX_N

    s, e = 0, 0
    while e < n and s <= e:  # O(n)
        partSum = dp[e] - dp[s] + arr[s]

        if bias > partSum:
            e += 1
        else:
            # print(f"arr[{s}:{e+1}] : {arr[s:e+1]}, sum : {partSum}")
            ans = min(ans, e - s + 1)

            s += 1

    print(ans if ans != MAX_N else 0)
