import sys

input = sys.stdin.readline

n, m = map(int, input().split())
d = []

for i in range(n):
    arr = [*map(int, input().split())]
    
    for j in range(m):
        if arr[j] == 1: d.append([i, j])

print(abs(d[0][0] - d[1][0]) + abs(d[0][1] - d[1][1]))