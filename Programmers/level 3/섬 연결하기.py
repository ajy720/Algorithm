from heapq import heappush, heappop, heapify
from collections import deque


def solution(n, costs):
    answer = 0

    graph = [[] for _ in ' '*n]

    for a, b, weight in costs:
        heappush(graph[a], (weight, b))
        heappush(graph[b], (weight, a))

    visit = [False]*n
    hq = [(0, 0)]

    while hq:
        weight, node = heappop(hq)

        if visit[node]:
            continue

        visit[node] = True
        answer += weight

        for nextWeight, nextNode in graph[node]:
            heappush(hq, (nextWeight, nextNode))

    return answer


if __name__ == "__main__":
    print(solution(4, [[0, 1, 1], [0, 2, 2], [1, 2, 5], [1, 3, 1], [2, 3, 8]]))
