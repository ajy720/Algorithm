import sys


if __name__ == "__main__":
    n = int(input())
    arr = [*map(int, input().split())]
    res = 0
    minimum = sys.maxsize

    for x in arr:
        minimum = min(x, minimum)
        res = max(res, x - minimum)

    print(res)
