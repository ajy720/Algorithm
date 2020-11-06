import sys
from queue import PriorityQueue

input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())

    arr = sorted([[*map(int, input().split())] for _ in ' '*n])

    l, p = map(int, input().split())

    q = PriorityQueue()
    idx = 0 
    cnt = 0 
    while l > p:

        while idx < n and arr[idx][0] <= p:
            q.put(-arr[idx][1])
            idx += 1
        
        if q.empty():
            break
            
        p -= q.get()
        cnt += 1 

    print(cnt if l <= p else -1)