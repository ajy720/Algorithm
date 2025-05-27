from math import sqrt

if __name__ == "__main__":
    n, k = map(int, input().split())
    res = set()

    for i in range(1, int(sqrt(n)) + 1):
        if n % i == 0:
            res.add(i)
            res.add(n // i)

    if len(res) > k - 1:
        print(sorted(list(res))[k - 1])
    else:
        print(0)
