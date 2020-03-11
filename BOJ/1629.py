def pow(a, n):
    global c
    if n == 0: return 1

    if n % 2 == 0: return (pow(a, n//2)**2)%c
    else: return (a*pow(a, n-1))%c

a, b, c = map(int, input().split())

print(pow(a, b)%c)