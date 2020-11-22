import sys
import heapq

input = sys.stdin.readline

def solve():
    cost = [sys.maxsize] * n
    cost[s] = 0
    is_pass = [False] * n

    q = []
    heapq.heappush(q, (0, s))

    while q:
        weight, node = heapq.heappop(q)

        while arr[node]:
            nextWeight, nextNode = heapq.heappop(arr[node])
            nextWeight += weight
            if cost[nextNode] >= nextWeight:
                cost[nextNode] = nextWeight
                heapq.heappush(q, (nextWeight, nextNode))

                if is_pass[node] or nextNode in [g, h] and node in [g, h]:
                    is_pass[nextNode] = True

    
    print(*sorted([i+1 for i in arrival if is_pass[i]]))

    
if __name__ == "__main__":
    for _ in ' '*int(input()):
        n, m, t = map(int, input().split())
        s, g, h = map(lambda x: int(x)-1, input().split())

        arr = [[] for _ in ' '*n]

        for _ in ' '*m:
            a, b, weight = map(int, input().split())
            heapq.heappush(arr[a-1], (weight, b-1))
            heapq.heappush(arr[b-1], (weight, a-1))

        arrival = [int(input())-1 for _ in ' '*t]

        solve()