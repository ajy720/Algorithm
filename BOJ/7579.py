n, k = map(int, input().split())

mem = [*map(int, input().split())]
cost = [*map(int, input().split())]
m = sum(cost)

arr = [[0] * (m) for i in range(n)]
ans = m

for i in range(n):
    for j in range(m):
        if j >= cost[i]:
            arr[i][j] = max(arr[i-1][j], arr[i-1][j-cost[i]] + mem[i])
        else:
            arr[i][j] = arr[i-1][j]
        
        if arr[i][j] >= k: ans = min(ans, j)

print(ans)