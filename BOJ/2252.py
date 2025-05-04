from sys import stdin

imput = stdin.readline


def dfs(curr, stack):
    global graph

    visit[curr] = True

    for x in graph[curr]:
        if visit[x]:
            continue

        dfs(x, stack)

    stack.append(curr + 1)
    return stack


if __name__ == "__main__":
    n, m = map(int, input().split())

    graph = [[] for _ in range(n)]  # 순방향, 역방향
    visit = [0] * n  # 방문 여부 겸 깊이 값

    for _ in range(m):
        a, b = map(lambda x: int(x) - 1, input().split())

        graph[a].append(b)
    stack = []
    for i in range(n):
        if visit[i]:
            continue

        stack = dfs(i, stack)

    print(*stack[::-1])
