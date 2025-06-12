from math import sqrt


def isRSA(n):

    divisors = set()
    for i in range(1, int(sqrt(n)) + 1):

        if n % i == 0:
            divisors.add(i)
            divisors.add(n // i)

    return len(divisors) == 4


if __name__ == "__main__":
    a = int(input())
    b = int(input())
    ans = len([True for i in range(a, b + 1) if isRSA(i)])

    print(f"The number of RSA numbers between {a} and {b} is {ans}")
