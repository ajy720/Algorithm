from collections import deque

dp = deque([1, 1])

for _ in ' '*int(input()):
    n = int(input())

    while dp[0] < n:
        dp.appendleft(dp[0] + dp[1])
    
    print(len(dp) - dp.index(n))
