MAX = 10002
filt = [False, False] + [True]*(MAX-1)
prime = []
for i in range(2, MAX):
    if filt[i]:
        prime.append(i)
        for j in range(i*2, MAX+1, i):
            filt[j] = False

m = int(input())
n = int(input())

prime = [i for i in range(m, n+1) if filt[i]]

if prime:
    print(sum(prime))
    print(min(prime))
else:
    print(-1)