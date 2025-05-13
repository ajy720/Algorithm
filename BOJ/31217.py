import sys

input = sys.stdin.readline

n, m = 0, 0
graph = {}
ans = 0

bias = 10**9 + 7

if __name__ == "__main__":

    n, m = map(int, input().split())
    graph = dict()

    for _ in range(m):
        a, b = map(int, input().split())
        Anodes = graph.setdefault(a, [])
        Anodes.append(b)
        Bnodes = graph.setdefault(b, [])
        Bnodes.append(a)

    for key, value in graph.items():
        l = len(value)
        ans += ((l * (l - 1) * (l - 2)) // 6) % bias
    print(ans % bias)
