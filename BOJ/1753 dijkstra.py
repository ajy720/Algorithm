import sys
from collections import deque
import heapq

input = sys.stdin.readline

def dijkstra(k):
    q = []

    ans[k] = 0

    heapq.heappush(q, (0, k))
    
    while q:
        weight, node = heapq.heappop(q)
        
        while arr[node]:
            nextWeight, nextNode = heapq.heappop(arr[node])
            nextWeight += weight
            
            if ans[nextNode] == 'INF' or ans[nextNode] > nextWeight:
                ans[nextNode] = nextWeight
                heapq.heappush(q, (nextWeight, nextNode))
            else:
                continue


if __name__ == "__main__":
    v, e = map(int, input().split())
    k = int(input()) - 1
    arr = [[] for _ in range(v)]
    ans = ['INF'] * v

    for _ in range(e):
        start, end, weight = map(int, input().split())
        start -= 1
        end -= 1
        heapq.heappush(arr[start], (weight, end))

    dijkstra(k)

    print(*ans, sep="\n")