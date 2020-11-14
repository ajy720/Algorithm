import sys
from collections import deque

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def bfs(k):
    dq = deque()

    ans[k] = 0
    
    for i in range(v):
        if arr[k][i]:
            dq.append((i, arr[k][i]))
            arr[k][i] = -1
    
    while dq:
        node, weight = dq.popleft()

        # if ans[node] > weight:
        #     ans[node] = weight 
        if ans[node] == -1:
            ans[node] = weight 
            
        for i in range(v):
            if arr[node][i]:
                dq.append((i, arr[node][i] + weight))
                arr[node][i] = -1


if __name__ == "__main__":
    v, e = map(int, input().split())
    k = int(input()) - 1
    arr = [[0] * v for _ in range(v)] 
    ans = [-1] * v

    for _ in range(e):
        start, end, weight = map(int, input().split())
        start -= 1
        end -= 1
        arr[start][end] = weight

    # for i in range(v):
    bfs(k)
    # print(out)

    for i in ans:
        print('INF' if i == -1 else i)