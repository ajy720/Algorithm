import sys

input = sys.stdin.readline

if __name__ == "__main__":
    n, k = map(int, input().split())
    arr = []
    dp = [0] * (k+1)

    for _ in range(n):
        t = int(input())
        if t <= k: 
            arr.append(t)
    
    arr.sort()

    for i in arr:
        dp[i] += 1
        for j in range(i+1, k+1):
            dp[j] += dp[j-i]

    print(dp[k])