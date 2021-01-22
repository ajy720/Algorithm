import sys

input = sys.stdin.readline

sys.setrecursionlimit(10**6)


def w(a, b, c):
    if dp[a][b][c]:
        return dp[a][b][c]

    if a <= 0 or b <= 0 or c <= 0:
        return 1

    if a > 20 or b > 20 or c > 20:        
        if not dp[20][20][20]:
            dp[20][20][20] = w(20, 20, 20)
        return dp[20][20][20]

    if a < b < c:
        dp[a][b][c] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
        return dp[a][b][c]

    else:
        dp[a][b][c] = w(a-1, b, c) + w(a-1, b-1, c) + \
            w(a-1, b, c-1) - w(a-1, b-1, c-1)
        return dp[a][b][c]


if __name__ == "__main__":
    dp = [[[0]*101 for i in range(101)] for i in range(101)]

    while 1:
        a, b, c = map(int, input().split())
        if a == -1 and b == -1 and c == -1:
            exit()

        print(f'w({a}, {b}, {c}) = {w(a, b, c)}')