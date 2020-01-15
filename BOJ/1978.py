from math import sqrt

input()
num = list(map(int, input().split()))
ans = 0
for n in num:
    if n == 1:
        continue
    elif n == 2:
        ans+=1
        continue

    flag = True

    for i in range(2, int(sqrt(n))+1):
        if n % i == 0:
            flag = False
            break
    if flag:
        ans += 1

print(ans)