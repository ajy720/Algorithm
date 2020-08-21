import math
import sys


input = sys.stdin.readline

primeN = []


def getPrime(n):
    global prime
    prime = [False, False] + [True] * (n-1)
    ret = [2, 3]

    for i in range(4, n+1, 2):
        prime[i] = False
    for i in range(6, n+1, 3):
        prime[i] = False

    for i in range(5, n+1, 6):
        if prime[i]:
            ret.append(i)
            for j in range(i*2, n+1, i):
                prime[j] = False

        r = i + 2
        if r <= n:
            if prime[r]:
                ret.append(r)
                for j in range(r*2, n+1, r):
                    prime[j] = False

        else:
            continue

    return ret


def is_prime(n):
    if n <= 2000000:
        return prime[n]
        
    for p in primeN:
        if n % p != 0:
            continue

        if p == n:
            break

        if n % p == 0:
            return False

    return True


if __name__ == "__main__":
    arr = [sum(map(int, input().split())) for _ in range(int(input()))]

    primeN = getPrime(2000000)

    for value in arr:
        if value == 2:
            print("NO")
            continue

        if value % 2 == 0:
            print("YES")
            continue

        if is_prime(value - 2):
            print("YES")

        else:
            print("NO")
