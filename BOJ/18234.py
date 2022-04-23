import sys

input = sys.stdin.readline


def solve():
    n, t = map(int, input().split())

    arr = []

    for _ in range(n):
        arr.append([*map(int, input().split())])

    arr = sorted(arr, key=lambda x: x[1], reverse=True)

    res = 0
    for idx, value in enumerate(arr):
        res += value[0] + value[1] * (t-idx-1)

    print(res)

    return


if __name__ == "__main__":
    solve()
