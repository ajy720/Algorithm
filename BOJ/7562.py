import sys
from collections import deque

input = sys.stdin.readline

px = [+2, +1, -1, -2, -2, -1, +1, +2]
py = [+1, +2, +2, +1, -1, -2, -2, -1]

for _ in range(int(input())):
    n = int(input())
    board = [[False]*n for _ in ' '*n]

    startX, startY = map(int, input().split())
    endX, endY = map(int, input().split())

    q = deque([(0, startX, startY)])

    while q:
        d, x, y = q.popleft()

        if x == endX and y == endY:
            print(d)
            break

        for i in range(8):
            ox = x + px[i]
            oy = y + py[i]

            if 0 <= ox < n and 0 <= oy < n:
                if not board[ox][oy]:
                    q.append((d+1, ox, oy))
                    board[ox][oy] = True
                