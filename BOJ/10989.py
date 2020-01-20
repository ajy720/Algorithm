import sys

input = sys.stdin.readline

arr = [0]*10001

for i in range(int(input())):
    arr[int(input())] += 1

for i, a in enumerate(arr):
    if a == 0: continue
    print(f"{i}\n"*a, end="")