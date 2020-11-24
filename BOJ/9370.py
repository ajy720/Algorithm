import sys
import heapq

input = sys.stdin.readline


def dijkstra(startNode):
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


def solve():
    start_ = dijkstra(s)
    g_ = dijkstra(g)
    h_ = dijkstra(h)

    print(*sorted([i for i in arrival
        if start_[i] == start_[g] + g_[h] + h_[i] 
        or start_[i] == start_[h] + h_[g] + g_[i]]))

    
if __name__ == "__main__":
    for _ in ' '*int(input()):
        n, m, t = map(int, input().split())
        s, g, h = map(int, input().split())

        arr = [[] for _ in ' '*(n+1)]

        for _ in ' '*m:
            a, b, weight = map(int, input().split())
            heapq.heappush(arr[a], (weight, b))
            heapq.heappush(arr[b], (weight, a))

        arrival = [int(input()) for _ in ' '*t]

        solve()
