import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

px = [-1, 0, 1, 0]
py = [ 0,-1, 0, 1]

def dfs(x, y):
    arr[x][y] = 0

    for i in range(4):
        ox = x+px[i]
        oy = y+py[i]
        if 0 <= ox < n and 0 <= oy < m and arr[ox][oy] == 1:
            dfs(ox, oy)

for _ in range(int(input())):
    n, m, k = map(int, input().split())
    ans = 0
    arr = [[0]*m for i in range(n)]

    for _ in range(k):
        x, y = map(int, input().split())
        arr[x][y] = 1

    for i in range(n):
        for j in range(m):
            if arr[i][j]:
                dfs(i, j)
                ans += 1
    
    print(ans)