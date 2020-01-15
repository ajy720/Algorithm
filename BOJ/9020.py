num = []
for _ in range(int(input())):
    num.append(int(input()))

prime = []
res = [False, False] + [True]*(max(num)-1)
for i in range(2, max(num)+1):
    if res[i]:
        prime.append(i)
        for j in range(2*i, max(num)+1, i):
            res[j] = False

for n in num:
    for i in range(n//2, 0, -1):
        if i in prime:
            flag = False
            for j in range(prime.index(i), len(prime)):
                if i + prime[j] == n:
                    print(i, prime[j])
                    flag = True
                    break
                elif i + prime[j] > n:
                    break

            if flag:
                break