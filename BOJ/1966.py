from collections import deque
import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))

    chk = [True if i == m else False for i in range(n)]

    cnt = 1
    while arr:
        i = arr.index(max(arr))
        arr = arr[i:] + arr[:i]
        chk = chk[i:] + chk[:i]

        arr.pop(0)
        if chk.pop(0):
            print(cnt)
            break
        cnt += 1