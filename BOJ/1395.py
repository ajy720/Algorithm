import sys

input = sys.stdin.readline

n, m = map(int, input().split())

sw = [False]*(n+1)

for _ in range(m):
    task, s, t = map(int, input().split())

    if task:
        print(sw[s:t+1].count(True))
    else:
        sw[s:t+1] = map(lambda x: not x, sw[s:t+1])