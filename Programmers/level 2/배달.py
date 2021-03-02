from collections import deque
from heapq import heappop, heappush
import sys


def solution(n, road, k):
    graph = [[] for _ in ' '*n]
    visit = [sys.maxsize] * n

    for a, b, weight in road:
        a -= 1
        b -= 1
        heappush(graph[a], (weight, b))
        heappush(graph[b], (weight, a))

    q = [(0, 0)]
    visit[0] = 0

    while q:
        weight, node = heappop(q)

        for nextWeight, nextNode in graph[node]:
            nextWeight += weight

            if visit[nextNode] > nextWeight:
                visit[nextNode] = nextWeight
                heappush(q, (nextWeight, nextNode))

    answer = len([i for i in visit if i <= k])

    return answer


if __name__ == "__main__":
    n = 5
    road = [[1, 2, 1], [2, 3, 3], [5, 2, 2], [1, 4, 2], [5, 3, 1], [5, 4, 2]]
    k = 3
    print(solution(n, road, k))

    n = 6
    road = [[1, 2, 1], [1, 3, 2], [2, 3, 2], [
        3, 4, 3], [3, 5, 2], [3, 5, 3], [5, 6, 1]]
    k = 4
    print(solution(n, road, k))
