import sys

input = sys.stdin.readline

if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input())
        arr = [*map(int, input().split())]

        matrix = [[0] * n for i in range(n)]

        for i in range(1, n):
            for j in range(0, n - i):
                matrix[i + j][j] = min(
                    [matrix[k][j] + matrix[j + i][k + 1] for k in range(j, j + i)]
                ) + sum(arr[j : j + i + 1])
        print(matrix[n - 1][0])
