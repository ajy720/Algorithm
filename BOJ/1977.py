from math import sqrt

n = int(input())
m = int(input())

ans = []

for i in range(int(sqrt(n)), int(sqrt(m))+1):
    if n <= i**2 <= m:
        ans.append(i**2)

if ans:
    print(sum(ans))
    print(ans[0])
else:
    print(-1)
