n = int(input())
ans = 0
t = 1
while t*10 <= n:
    ans += len(str(t))*9*t
    t = t * 10

ans += len(str(t))*(n-t+1)
print(ans)