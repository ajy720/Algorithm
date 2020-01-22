import sys

input = sys.stdin.readline

n = int(input())
arr = []
for i in range(n):
    x, y = map(int, input().split())
    arr.append(tuple([y, x]))

for x, y in sorted(arr):
    print(y, x)