import sys

input = sys.stdin.readline

n = int(input())
arr = [[] for i in range(51)]

for _ in range(n):
    temp = input().rstrip("\n")
    if temp not in arr[len(temp)]:
        arr[len(temp)].append(temp)

for i in arr:
    for j in sorted(i):
        print(j)