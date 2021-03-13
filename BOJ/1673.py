import sys

for i in sys.stdin.readlines():
    n, k = map(int, i.split())

    ans = 0
    while n >= k:
        ans += (n // k) * k
        n = n % k + n // k

    ans += n

    print(ans)
