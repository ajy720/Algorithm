import sys

input = sys.stdin.readline

n = int(input())
arr = []
for i in range(n):
    arr.append(tuple(map(int, input().split())))

for x, y in sorted(arr):
    print(x, y)