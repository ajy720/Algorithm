def gcd(a, b):
    while a and b:
        if a < b:
            a, b = b, a

        a %= b

    return b


def lcm(a, b):
    return a * b // gcd(a, b)


for _ in range(int(input())):
    print(lcm(*map(int, input().split())))
