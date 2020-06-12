from collections import deque

def dfs(n):
    for i in range(1, len(arr[n])):
        if (arr[n][i] or arr[i][n]) and arr[i][0] == 0:
            arr[i][0] = 1
            print(i, end=" ")
            dfs(i)

def bfs(n):
    while 1:
        if not dq:
            return

        n = dq.popleft()
        print(n, end=" ")

        for i in range(1, len(arr[n])):
            if (arr[n][i] or arr[i][n]) and arr[i][0] == 0:
                dq.append(i)
                arr[i][0] = 1


dq = deque()
n, m, v = map(int, input().split())
arr = [[0]*(n+1) for i in range(n+1)]

for i in range(m):
    x, y = map(int, input().split())
    arr[x][y] = 1
    arr[y][x] = 1

print(v, end=" ")
arr[v][0] = 1
dfs(v)
print()

for i in range(len(arr)):
    arr[i][0] = 0

arr[v][0] = 1
dq.append(v)
bfs(v)