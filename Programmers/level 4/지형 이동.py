from collections import deque
from heapq import heappop, heappush, heapify

px = [+1, -1,  0,  0]
py = [0,  0, -1, +1]

n = 0
group = 0
visit = []
land = []


def bfs(x, y, land, height):
    q = deque([(x, y)])

    while q:
        x, y = q.popleft()

        for i in range(4):
            ox = x + px[i]
            oy = y + py[i]

            if not(0 <= ox < n and 0 <= oy < n) or visit[ox][oy] != -1:
                continue

            if abs(land[ox][oy] - land[x][y]) > height:
                continue

            q.append((ox, oy))
            visit[ox][oy] = group


def solution(land, height):
    answer = 0

    global n, visit, group

    n = len(land)
    group = 0
    visit = [[-1]*n for _ in ' '*n]
    graph = []

    # 지도 그룹화
    for i in range(n):
        for j in range(n):
            if visit[i][j] != -1:
                continue

            visit[i][j] = group
            bfs(i, j, land, height)

            group += 1
            graph.append(dict())

    # 그룹 간 필요 사다리 최소비용
    for x in range(n):
        for y in range(n):
            for i in range(4):
                ox = x + px[i]
                oy = y + py[i]

                if not(0 <= ox < n and 0 <= oy < n):
                    continue

                a = visit[ox][oy]
                b = visit[x][y]

                if a != b:
                    t = abs(land[ox][oy] - land[x][y])

                    if b in graph[a]:
                        t = min(graph[a][b], t)

                    graph[a][b] = t

    # 그래프 전처리
    for i in range(len(graph)):
        graph[i] = [*zip(graph[i].values(), graph[i].keys())]
        heapify(graph[i])

    # 프림 알고리즘 활용
    visit = [False]*len(graph)

    visit[0] = True
    q = graph[0].copy()

    while q:
        weight, node = heappop(q)

        if visit[node]:
            continue

        visit[node] = True
        answer += weight

        for nextWeight, nextNode in graph[node]:
            heappush(q, (nextWeight, nextNode))

    return answer


if __name__ == "__main__":
    print(solution([[1, 4, 8, 10],
                    [5, 5, 5, 5],
                    [10, 10, 10, 10],
                    [10, 10, 10, 20]], 3), 15)

    print(solution([[10, 11, 10, 11],
                    [2, 21, 20, 10],
                    [1, 20, 21, 11],
                    [2, 1, 2, 1]], 1), 18)
