from collections import deque

px = [ 0, 1, 0,-1]
py = [-1, 0, 1, 0]

def bfs(i, j):
    q = deque()
    q.append([i, j])
    arr[i][j] = -1
    ret = 0

    while q:
        x, y = q.popleft()
        ret += 1

        for i in range(4):
            ox = x+px[i]
            oy = y+py[i]

            if 0 <= ox < n and 0 <= oy < n:
                if arr[ox][oy] == 1:
                    q.append([ox, oy])
                    arr[ox][oy] = -1
        
    return ret
                

if __name__ == "__main__":
    n = int(input())
    arr = [[int(j) for j in input()] for i in range(n)]
    ans = []

    for i in range(n):
        for j in range(n):
            if arr[i][j] == 1:
                ans.append(bfs(i, j))
    
    print(len(ans))
    for i in sorted(ans):
        print(i)