visit = []
answer = 0

def solution(n, computers):
    global answer, visit

    visit = [False] * n
    answer = 0

    for i in range(n):
       answer += dfs(0, i, computers)

    return answer

def dfs(depth, node, graph):
    if visit[node]:
        return 0

    visit[node] = True

    for i in range(len(graph)):
        if graph[node][i]:
            dfs(depth+1, i, graph)
    
    return 1


if __name__ == "__main__":
    print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]), 2)
    print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]), 1)
