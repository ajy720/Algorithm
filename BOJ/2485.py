import sys

input = sys.stdin.readline

def arrGcd(arr):
    while len(arr) > 1:
        t = []
        for i in range(0, len(arr), 2):
            try:
                t.append(gcd(arr[i], arr[i+1]))
            except:
                t.append(arr[i])

        arr = t.copy()

    return arr[0]


def gcd(a, b) -> int:
    while 1:
        if a < b:
            a, b = b, a

        a %= b

        if a == 0:
            return b


if __name__ == "__main__":
    n = int(input())
    arr = [int(input())]
    space = []

    for _ in ' '*(n-1):
        t = int(input())
        space.append(t-arr[-1])
        arr.append(t)

    d = arrGcd(space)
    print(sum([i//d-1 for i in space]))
