n = 0
board = []
dp = []


def pprint(arr):
    for row in arr:
        for cell in row:
            print(f"{cell:2d}", end=" ")
        print()


def process(x, y):

    global n, board

    if not board[x][y]:
        return

    next1 = (x + board[x][y], y)  # go down
    next2 = (x, y + board[x][y])  # go right

    nexts = [next for next in [next1, next2] if next[0] < n and next[1] < n]

    for next in nexts:
        # print(f"from {x, y} to {next[0], next[1]} : {dp[x][y]}")
        dp[next[0]][next[1]] += dp[x][y]


if __name__ == "__main__":
    n = int(input())

    board = [list(map(int, input().split())) for _ in range(n)]

    dp = [[0] * n for _ in range(n)]
    dp[0][0] = 1

    for i in range(n):
        for j in range(n):
            process(i, j)

    # pprint(dp)

    # dfs((0, 0), (n - 1, n - 1), [])

    print(dp[n - 1][n - 1])
