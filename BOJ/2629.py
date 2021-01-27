s = []
arr = []


def solve(n, ret):
    if s[n-1][ret]:
        return

    s[n-1][ret] = True

    if n >= len(arr):
        return

    solve(n+1, ret)
    solve(n+1, ret + arr[n])
    solve(n+1, ret - arr[n])


if __name__ == "__main__":
    n = int(input())
    arr = [*map(int, input().split())]

    s = [[False] * (55001) for _ in range(n)]

    solve(0, 0)

    input()
    print(*['Y' if s[n-1][t] else 'N' for t in map(int, input().split())])
