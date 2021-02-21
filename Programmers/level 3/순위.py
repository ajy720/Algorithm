import sys

sys.setrecursionlimit(10**6)


def dfs(k, flag):
    graph = graph1 if flag else graph2
    dp = dp1 if flag else dp2

    if dp[k]:
        return dp[k]

    for i in graph[k]:
        dp[k].update(dfs(i, flag))

    dp[k].update(graph[k])

    return dp[k]


def solution(n, results):
    answer = 0

    global graph1, graph2, dp1, dp2

    graph1 = [set() for _ in ' '*n]
    graph2 = [set() for _ in ' '*n]
    dp1 = [set() for _ in ' '*n]
    dp2 = [set() for _ in ' '*n]

    for win, lose in results:
        graph1[win-1].add(lose-1)
        graph2[lose-1].add(win-1)

    for i in range(n):
        t = len(dfs(i, True).union(dfs(i, False)))

        if t == n-1:
            answer += 1

    return answer


print(solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))
