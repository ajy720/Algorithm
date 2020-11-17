import sys
import heapq

input = sys.stdin.readline

def dijkstra(arr, start, ret):
    q = []

    cost = [-1] * n
    cost[start] = 0

    heapq.heappush(q, (0, start))
    
    while q:
        weight, node = heapq.heappop(q)
        
        for nextWeight, nextNode in arr[node]:
            nextWeight += weight
            
            if cost[nextNode] == -1 or cost[nextNode] > nextWeight:
                cost[nextNode] = nextWeight
                heapq.heappush(q, (nextWeight, nextNode))
            else:
                continue

    return [cost[i] for i in ret]

if __name__ == "__main__":
    n, e = map(int, input().split())

    arr = [[] for _ in ' '*n]
    ans = 0


    for _ in range(e):
        start, end, weight = map(int, input().split())
        heapq.heappush(arr[start-1], (weight, end-1))
        heapq.heappush(arr[end-1], (weight, start-1))

    v1, v2 = map(lambda x: int(x)-1, input().split())

    graph = [[] for _ in ' '*n]

    start_v1, v_v, end_v1 = dijkstra(arr, v1, [0, v2, n-1])
    start_v2, end_v2 = dijkstra(arr, v2, [0, n-1])

    if -1 in [start_v1, start_v2, end_v1, end_v2, v_v]:
        ans = -1
    else:    
        ans = min(
            start_v1 + v_v + end_v2,
            start_v2 + v_v + end_v1,
            start_v1 + v_v + v_v + end_v2,
            start_v2 + v_v + v_v + end_v1
        )
    
    print(ans)