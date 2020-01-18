from math import ceil

def ext_euc(a, b):
    if b == 0:
        return a, 1, 0
    g, x, y = ext_euc(b, a%b)
    return g, y, x-(a//b)*y
    
a, b, s = map(int, input().split())

if a == 0 and b == 0:
    print("YES" if s == 0 else "NO")
    exit()

if a == 0:
    print("YES" if s % b == 0 else "NO")
    exit()

if b == 0:
    print("YES" if s % a == 0 else "NO")
    exit()

gcd, p, q = ext_euc(a, b)

if s % gcd != 0:
    print("NO")
    exit()
unit = s//gcd
p, q = p*(unit), q*(unit)

n = ceil(max(-p*(gcd/b), q*(gcd/a)))
m = ceil(min(-p*(gcd/b), q*(gcd/a)))

if n == m:
    print("NO")
    exit()

#print(range(m, n))
for i in range(m, n):
    j=(p+(b//gcd)*i)
    k=(q+(-a//gcd)*i)
    
    #print(j, k)
    if k > j:
        k, j = j, k

    if ext_euc(j, k)[0]==1:
        print("YES")
        exit()

print("NO")