import sys
import heapq
 
input = sys.stdin.readline
 
 
def dijkstra(startNode, n):
    cost = [sys.maxsize] * (n+1)
    cost[startNode] = 0
 
    q = [] # (weight, node) 우선순위 큐
 
    heapq.heappush(q, (0, startNode))
 
    while q:
        weight, node = heapq.heappop(q)
 
        for nextWeight, nextNode in arr[node]:
            nextWeight += weight
            if nextWeight < cost[nextNode]:
                cost[nextNode] = nextWeight
                heapq.heappush(q, (nextWeight, nextNode))
 
    return cost
 
 
if __name__ == "__main__":
    v, e = map(int, input().split())
    k = int(input()) - 1
    arr = [[] for _ in range(v)]
 
    for _ in range(e):
        start, end, weight = map(int, input().split())
        start -= 1
        end -= 1
        heapq.heappush(arr[start], (weight, end))
 
    print(*dijkstra(k, v), sep="\n")