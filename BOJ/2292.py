x = int(input())
n = 1
cnt = 1
while x > n:
    cnt += 1
    n = n + 6*(cnt-1)

print(cnt)