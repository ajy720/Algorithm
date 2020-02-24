import sys
input = sys.stdin.readline

n, k = map(int, input().split())
w = [0] + [0] * n
v = [0] + [0] * n
arr = [[0] * (k+1) for i in range(n+1)] 

for i in range(1, n+1):
    w[i], v[i] = map(int, input().split())

for i in range(1, n+1):
    for j in range(1, k+1):
        if j >= w[i]: arr[i][j] = max(arr[i-1][j-w[i]]+v[i], arr[i-1][j])
        else: arr[i][j] = arr[i-1][j]

print(arr[n][k])