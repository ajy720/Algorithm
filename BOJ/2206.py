from collections import deque
from copy import deepcopy

px = [-1, 0, 1, 0]
py = [ 0,-1, 0, 1]

def bfs():

    while q:
        x, y, b, d = q.popleft()

        if x == n-1 and y == m-1:
            return d

        for i in range(4):
            ox = x + px[i]
            oy = y + py[i]

            if 0 <= ox < n and 0 <= oy < m and chk[ox][oy][b]:
                if arr[ox][oy] == 0:
                    q.append((ox, oy, b, d+1))
                    chk[ox][oy][b] = 0
                
                elif arr[ox][oy] == 1 and b:
                    q.append((ox, oy, 0, d+1))
                    chk[ox][oy][b] = 0
    
    return -1
            



if __name__ == "__main__":
    n, m = map(int, input().split())
    arr = [[int(i) for i in input()] for _ in ' '*n]
    chk = [[[1, 1] for i in range(m)] for _ in range(n)]

    q = deque([(0, 0, 1, 1)])

    print(bfs())
    