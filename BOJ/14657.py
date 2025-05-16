import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)


def dfs(curr, depth, cost):
    global graph, visit
    global max_depth, min_cost, max_node

    if visit[curr]:
        return curr, depth, cost

    visit[curr] = True
    depth = depth + 1

    # print(f"Visit {curr}, depth: {depth}, cost: {cost}")

    local_depth = depth
    local_node = curr
    local_cost = cost

    for next, weight in graph[curr].items():
        if visit[next]:
            continue

        res_node, res_depth, res_cost = dfs(next, depth, cost + weight)
        if res_depth > local_depth:
            local_depth = res_depth
            local_node = res_node
            local_cost = res_cost

    # print(f"maxnode: {local_node}, maxdepth: {local_depth}, mincost: {local_cost}")
    if local_depth > max_depth or (local_depth == max_depth and local_cost < min_cost):
        # print(f"Update")

        max_depth = local_depth
        max_node = local_node
        min_cost = local_cost

    return local_node, local_depth, local_cost


if __name__ == "__main__":
    n, t = map(int, input().split())

    graph = [dict() for _ in range(n)]

    for _ in range(n - 1):
        a, b, w = map(int, input().split())
        graph[a - 1].setdefault(b - 1, w)
        graph[b - 1].setdefault(a - 1, w)

    # print("Graph :", graph)

    visit = [False] * n
    max_depth, min_cost, max_node = 0, sys.maxsize, 0
    edge_node, edge_path, edge_cost = dfs(0, 0, 0)

    visit = [False] * n
    max_depth, min_cost, _ = 0, sys.maxsize, 0
    dfs(max_node, 0, 0)

    print(min_cost // t + (1 if min_cost % t else 0))
