from collections import deque

BLANK = 0
FILLED = 1

px = [-1, 0, 1, 0]
py = [0, -1, 0, 1]


def bfs(x, y):
    size = 1
    q = deque()
    arr[x][y] = FILLED
    q.append((x, y))

    while q:
        x, y = q.popleft()

        for i in range(4):
            ox = x + px[i]
            oy = y + py[i]

            if 0 <= ox < n and 0 <= oy < m and arr[ox][oy] == BLANK:
                arr[ox][oy] = FILLED
                q.append((ox, oy))
                size += 1

    return size


if __name__ == "__main__":
    m, n, k = map(int, input().split())
    arr = [[BLANK] * m for _ in range(n)]
    ans = []

    for _ in range(k):
        x1, y1, x2, y2 = map(int, input().split())

        for i in range(x1, x2):
            arr[i][y1:y2] = [FILLED] * (y2-y1)

    for i in range(n):
        for j in range(m):
            if arr[i][j] == BLANK:
                ans.append(bfs(i, j))

    print(len(ans))
    print(*sorted(ans))
