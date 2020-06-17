if __name__ == "__main__":
    n = int(input())

    arr = [*map(int, input().split())]
    dp = [arr[0]] + [0] * (n-1)


    for i in range(1, n):
        try:
            dp[i] = max([dp[j] for j in range(i) if arr[j] < arr[i]]) + arr[i]
        except:
            dp[i] = arr[i]

    print(max(dp))