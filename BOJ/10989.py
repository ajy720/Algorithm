import sys

input = sys.stdin.readline

arr = [0]*10001

for i in range(int(input())):
    arr[int(input())] += 1

for i in range(1, 10001):
    if arr[i] == 0: continue
    for _ in range(arr[i]):
        print(i)