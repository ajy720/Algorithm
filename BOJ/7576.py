import sys
from collections import deque

input = sys.stdin.readline

px = [ 1, 0,-1, 0]
py = [ 0, 1, 0,-1]
d = 0

def bfs():
    while dq:
        t = dq.popleft()
        x = t[0]
        y = t[1]
        d = t[2]

        for i in range(4):
            ox = x + px[i]
            oy = y + py[i]
            if 0 <= ox < m and 0 <= oy < n and arr[ox][oy] == 0:
                arr[ox][oy] = -1
                dq.append((ox, oy, d+1))
    
    for l in arr:
        if 0 in l:
            print(-1)
            return

    print(d)

if __name__ == "__main__":
    n, m = map(int, input().split())

    arr = []
    dq = deque()
    
    for i in range(m):
        t = [*map(int, input().split())]
        arr.append(t)
        for j in range(len(t)):
            if t[j] == 1:
                dq.append((i, j, d))
    
    bfs()