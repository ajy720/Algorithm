import sys

sys.setrecursionlimit(10000)
input = sys.stdin.readline

px = [0, 1, 0, -1]
py = [-1, 0, 1, 0]


def dfs(x, y):
    ret = 0
    if x == n - 1 and y == m - 1:
        return 1

    if dp[x][y] != -1:
        return dp[x][y]

    for i in range(4):
        if (
            0 <= y + py[i] < m
            and 0 <= x + px[i] < n
            and arr[x + px[i]][y + py[i]] < arr[x][y]
        ):
            ret += dfs(x + px[i], y + py[i])

    dp[x][y] = ret

    return ret


if __name__ == "__main__":
    n, m = map(int, input().split())

    arr = [[*map(int, input().split())] for i in range(n)]
    dp = [[-1] * m for i in range(n)]

    print(dfs(0, 0))
