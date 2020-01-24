n, m = map(int, input().split())

temp = n * m

while n != 0:
    if n < m: n, m = m, n
    n = n%m

print(m)
print(temp//m)