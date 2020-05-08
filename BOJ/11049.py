import sys

input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    arr = [[*map(int, input().split())] for _ in range(n)]

    matrix = [[0] * n for i in range(n)]

    for i in range(1, n):
        for j in range(0, n - i):
            matrix[i + j][j] = min(
                [
                    matrix[k][j]
                    + matrix[j + i][k + 1]
                    + (arr[j][0] * arr[k + 1][0] * arr[j + i][1])
                    for k in range(j, j + i)
                ]
            )

    print(matrix[n - 1][0])