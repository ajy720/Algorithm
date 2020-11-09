import sys
from queue import PriorityQueue

input = sys.stdin.readline

if __name__ == "__main__":
    n, k = map(int, input().split())

    arr = sorted([[*map(int, input().split())] for _ in ' '*n], reverse=True, key=lambda x: x[1])
    bags = sorted([int(input()) for _ in ' '*k])

    ans = 0 

    i, j = 0, 0
    dq = PriorityQueue()

    for bag in bags:
        while i < n and arr[i][0] <= bag:
            dq.put(-arr[i][1])
            i += 1
        
        if dq:
            ans -= dq.get()

    print(ans)
