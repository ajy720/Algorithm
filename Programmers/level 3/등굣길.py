def solution(m, n, puddles):
    arr = [[0]*m for _ in ' '*n]
    arr[0][0] = 1

    for x, y in puddles:
        arr[y-1][x-1] = -1

    for t in range(m+n-1):
        for p in range(t+1):
            x = t-p
            y = p

            if not(0 <= x < n and 0 <= y < m) or arr[x][y] == -1:
                continue

            arr[x][y] %= 1000000007

            if x+1 < n and arr[x+1][y] != -1:
                arr[x+1][y] += arr[x][y]

            if y+1 < m and arr[x][y+1] != -1:
                arr[x][y+1] += arr[x][y]

    print(*arr, sep='\n')

    return arr[-1][-1] % 1000000007


if __name__ == "__main__":

    m, n = map(int, input().split())
    puddles = []
    for _ in ' '*int(input()):
        puddles.append([*map(int, input().split())])

    print(solution(m, n, puddles))
