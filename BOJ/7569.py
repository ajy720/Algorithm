from collections import deque

px = [ 1, 0, 0,-1, 0, 0]
py = [ 0, 1, 0, 0,-1, 0]
pz = [ 0, 0, 1, 0, 0,-1]


def bfs():
    global arr, q, n, m, h
    z, y, x = 0, 0, 0
    
    while q:
        z, y, x = q.popleft()

        for i in range(6):
            ox = x + px[i]
            oy = y + py[i]
            oz = z + pz[i]
            if 0 <= ox < n and 0 <= oy < m and 0 <= oz < h:
                if arr[oz][oy][ox] == 0:
                    q.append((oz, oy, ox))
                    arr[oz][oy][ox] = arr[z][y][x] + 1

    ret = arr[z][y][x] - 1

    for i in range(h):
        for j in range(m):
            for k in range(n):
                if arr[i][j][k] == 0:
                    ret = -1

    return ret


n, m, h = map(int, input().split())
arr = [[[0]*n for i in ' '*m] for i in ' '*h]
q = deque()

for i in range(h):
    for j in range(m):
        arr[i][j] = [*map(int, input().split())]
        for k in range(n):
            if arr[i][j][k] == 1:
                q.append((i, j, k))

print(bfs())
