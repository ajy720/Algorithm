def getPrime(n):
    prime = [False, False] + [True] * (n-1)
    ret = []
    for i in range(2, n+1):
        if prime[i]:
            ret.append(i)
            for j in range(i*2, n+1, i):
                prime[j] = False
        else:
            continue
    return ret
