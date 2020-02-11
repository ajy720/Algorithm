c, k, p = map(int, input().split())
sum = 0

for i in range(1, c+1):
    sum += (i*(k+p*i))

print(sum)