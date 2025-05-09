from sys import maxsize

moves = [
    [(1, -1), (1, 0)],
    [(1, -1), (1, 0), (1, 1), (0, 1)],
    [(1, 0), (1, 1), (0, 1)],
]


def solve(n: int):

    dp = [[maxsize] * 3 for _ in range(n)]

    for x in range(n):
        row = list(map(int, input().split()))
        if x == 0:
            dp[x] = [
                maxsize,
                row[1],
                row[2] + row[1],
            ]
            continue

        for y, value in enumerate(row):
            for px, py in moves[y]:
                dp[x][y] = min(dp[x][y], dp[x - px][y - py] + value)

    return dp[n - 1][1]


if __name__ == "__main__":
    T = 0
    while True:
        T += 1
        n = int(input())

        if n == 0:
            break

        print(f"{T}. {solve(n)}")
