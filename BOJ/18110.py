from sys import stdin
import math


input = stdin.readline


def round2(n):
    return math.floor(n + 0.5)


if __name__ == "__main__":
    n = int(input())

    arr = [int(input()) for _ in range(n)]

    arr.sort()
    cutting = round2(n * 0.15)
    arr = arr[cutting : -cutting if cutting else None]
    # print(arr)

    print(round2(sum(arr) / len(arr)) if arr else 0)
