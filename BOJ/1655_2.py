import heapq
import sys

input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    bHeap = []
    sHeap = []
    mid = sys.maxsize
    
    for _ in ' '*n:
        o = int(input())

        if o <= mid:
            heapq.heappush(sHeap, -o)
        else:
            heapq.heappush(bHeap, o)
        
        if len(bHeap) > len(sHeap):
            heapq.heappush(sHeap, -heapq.heappop(bHeap))
        elif len(sHeap) > len(bHeap) + 1:
            heapq.heappush(bHeap, -heapq.heappop(sHeap))
        
        mid = -sHeap[0]

        print(mid)
