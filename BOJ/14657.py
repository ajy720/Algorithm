from collections import deque
import sys

def dfs(start, depth):
    dp[start][2] = True
    dp[start][1] = depth
    for v, weight in graph[start]:
        if dp[v][2]:
            continue
            
        dfs(v, depth + 1)

        if dp[v][1] > dp[start][1]:
            dp[start][1] = dp[v][1]
            dp[start][0] = dp[v][0] + weight
        elif dp[v][1] == dp[start][1] and dp[v][0] + weight < dp[start][0]:
            dp[start][1] = dp[v][1]
            dp[start][0] = dp[v][0] + weight


if __name__ == "__main__":
    n, t = map(int, input().split())
    graph = [[] for _ in ' '*n]
    dp = [[0, 0, False] for _ in ' '*n]

    for _ in ' '*(n-1):
        a, b, w = map(int, input().split())
        a -= 1
        b -= 1

        graph[a].append((b, w))
        graph[b].append((a, w))
    
    dfs(0, 0)

    print(dp[0][0]//t+1)
