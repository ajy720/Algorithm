import sys
from collections import deque

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def bfs(k):
    dq = deque()

    ans[k] = 0
    
    while arr[k]:
        node, weight = arr[k].pop()
        ans[node] = weight
        dq.append((node, weight))
    
    while dq:
        node, weight = dq.popleft()
        
        if ans[node] > weight or ans[node] == -1:
            ans[node] = weight 
        
        while arr[node]:
            nextNode, nextWeight = arr[node].popleft()
            dq.append((nextNode, weight + nextWeight))


if __name__ == "__main__":
    v, e = map(int, input().split())
    k = int(input()) - 1
    arr = [deque() for _ in range(v)]
    ans = [-1] * v

    for _ in range(e):
        start, end, weight = map(int, input().split())
        start -= 1
        end -= 1
        arr[start].append((end, weight))

    # for i in range(v):
    bfs(k)
    # print(out)

    for i in ans:
        print('INF' if i == -1 else i)