from math import sqrt

for _ in range(int(input())):  
    x, y = map(int, input().split())
    n = y-x
    a = int(sqrt(n))

    ans = 0
    if a**2 == n:
        ans = 2*a - 1
    elif n <= a**2 + a:
        ans = 2*a
    elif n > a**2 + a:
        ans = 2*a + 1

    print(ans)