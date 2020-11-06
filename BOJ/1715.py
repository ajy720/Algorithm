import sys
import queue

input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    arr = queue.PriorityQueue()

    for _ in ' '*n:
        arr.put(int(input()))

    if n == 1:
        print(0)
        exit()

    ans = 0

    while arr.qsize() > 1:
        a = arr.get()
        b = arr.get()

        stack = a + b
        ans += stack
        arr.put(stack)

    print(ans)
