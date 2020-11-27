import sys

INF = sys.maxsize

input = sys.stdin.readline


def bellmanFord(startNode, edge):
	cost = [INF] * (n + 1)

	cost[startNode] = 0

	for _ in " " * (n - 1):
		for start, destination, weight in edge:
			if cost[start] != INF and cost[destination] > cost[start] + weight:
				cost[destination] = cost[start] + weight

	for start, destination, weight in edge:
		if cost[start] != INF and cost[destination] > cost[start] + weight:
			return False
	
	return [i if i != INF else -1 for i in cost]


if __name__ == "__main__":
	n, m = map(int, input().split())

	edge = [[*map(int, input().split())] for _ in ' '*m]
	
	res = bellmanFord(1, edge)

	if res:
		print(*res[2:], sep='\n')
	else:
		print(-1)
