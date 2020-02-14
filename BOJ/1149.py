import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)
minv = sys.maxsize

def dfs(x, cur):
    temp = []
    if x == 0:
        for i in range(3):
            if i == cur: continue
            temp.append(arr[x][i])
        return min(temp)

    for i in range(3):
        if i == cur: continue

        if not sarr[x][i]: sarr[x][i] = dfs(x-1, i) + arr[x][i]

        temp.append(sarr[x][i])

    return min(temp)

n = int(input())

arr = []

for _ in range(n):
    arr.append(list(map(int, input().split())))

sarr = [[0, 0, 0] for i in range(n)]

sarr[0] = arr[0]

for i in range(3):
    minv = min(minv, dfs(n-1, i))

print(minv)