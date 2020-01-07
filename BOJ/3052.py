import sys

n = list(map(int, sys.stdin.readlines()))
res = [0] * 42
cnt = 0

for i in n:
    if res[i%42]==0:
        cnt+=1
    res[i%42] += 1

print(cnt)