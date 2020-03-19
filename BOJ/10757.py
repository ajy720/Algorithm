def numlist(n):
    n = int(n)
    arr = []
    while n:
        arr.append(n%10)
        n//=10
    return arr+[0]

a, b = map(numlist, input().split())

if len(a) < len(b): a += [0]*abs(len(a)-len(b))    
else: b += [0]*abs(len(a)-len(b))

for i in range(len(a)-1):
    a[i+1] += (a[i] + b[i])//10
    a[i] = (a[i] + b[i])%10

if a[-1] == 0: a.pop(-1)

for i in range(1, len(a)+1):
    print(a[-i], end="")