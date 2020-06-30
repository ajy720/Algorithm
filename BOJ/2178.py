px = [ 0, 1, 0,-1]
py = [ 1, 0,-1, 0]
q = []

def bfs():
    while q:
        x, y, d = q.pop(0)
        if x == n-1 and y == m-1:
            print(d)
            break


        for i in range(4):
            ox = x+px[i]
            oy = y+py[i]
            if 0 <= ox < n and 0 <= oy < m and arr[ox][oy] == 1:
                q.append((ox, oy, d+1))
                arr[ox][oy] = -1


if __name__ == "__main__":
    n, m = map(int, input().split())
    arr = [[] for i in range(n)]

    for i in range(n):
        for j in input():
            arr[i].append(int(j))

    q.append((0, 0, 1))
    arr[0][0] = -1
    bfs()