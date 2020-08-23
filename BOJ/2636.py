from collections import deque

px = [-1, 0, 1, 0]
py = [0, -1, 0, 1]


def bfs():
    last, ans = 0, 0
    while 1:
        q = deque([(0, 0)])
        melt = []
        chk = [[0] * m for i in range(n)]

        while q:
            x, y = q.popleft()

            for i in range(4):
                ox = x + px[i]
                oy = y + py[i]

                if not(0 <= ox < n) or not(0 <= oy < m) or chk[ox][oy]:
                    continue

                if arr[ox][oy] == 0:
                    chk[ox][oy] = 1
                    q.append((ox, oy))

                if arr[ox][oy] == 1:
                    chk[ox][oy] = 1
                    melt.append((ox, oy))

        if not melt:
            return ans, last
        else:
            for x, y in melt:
                arr[x][y] = 0

            ans += 1
            last = len(melt)


if __name__ == "__main__":
    n, m = map(int, input().split())

    arr = [[*map(int, input().split())] for i in range(n)]
    print(*bfs(), sep="\n")
