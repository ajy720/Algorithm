from collections import deque


def solution(n, edge):
    answer = 0
    maxDepth = 0

    graph = [[] for _ in ' '*(n+1)]
    visit = [False]*(n+1)

    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)

    q = deque([(0, 1)])
    visit[1] = True

    while q:
        depth, node = q.popleft()

        if depth > maxDepth:
            maxDepth = depth
            answer = 1

        elif depth == maxDepth:
            answer += 1

        for nextNode in graph[node]:
            if not visit[nextNode]:
                q.append((depth+1, nextNode))
                visit[nextNode] = True

    return answer


if __name__ == "__main__":
    n = 6
    edge = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
    print(solution(n, edge))
