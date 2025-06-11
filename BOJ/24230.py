from sys import stdin

input = stdin.readline


def dfs(cur):
    global colors, graph, visit

    visit[cur] = 1

    for next in graph[cur]:
        if not visit[next] and colors[next] == colors[cur]:
            dfs(next)


if __name__ == "__main__":
    n = int(input())

    colors = list(map(int, input().split()))
    graph = [[] for _ in range(n)]
    visit = [0] * (n)

    ans = 0

    for _ in range(n - 1):
        a, b = map(lambda x: int(x) - 1, input().split())

        graph[a].append(b)
        graph[b].append(a)

    for i in range(n):
        if visit[i]:
            continue

        else:
            if colors[i] != 0:
                ans += 1
            dfs(i)

    print(ans)
