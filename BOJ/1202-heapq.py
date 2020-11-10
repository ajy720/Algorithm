import sys
import heapq

input = sys.stdin.readline

if __name__ == "__main__":
	n,k = map(int,input().split())

	arr = sorted([[*map(int, input().split())] for _ in ' '*n])
	bags = sorted([int(input()) for _ in ' '*k])

	ans = 0
	i = 0
	pq=[]

	for bag in bags:
		while i < n and arr[i][0] <= bag:
			heapq.heappush(pq,-arr[i][1])
			i+=1

		if pq:
			ans -= heapq.heappop(pq)

	print(ans)