n, m, k = map(int, input().split())

n //= 2

if n > m:
    k -= (n - m)*2
    n = m
else:
    k -= (m-n)
    m = n

while k > 0:
    n -= 1
    m -= 1
    k -= 3

print(m)