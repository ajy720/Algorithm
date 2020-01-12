n = int(input())

ans = temp = 0

for i in range(n//3+1):
    temp = n - 3*i
    if temp % 5 != 0:
        continue
    else:
        ans = i + temp//5
        break

print(ans if ans != 0 else -1)