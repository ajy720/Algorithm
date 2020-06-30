from collections import deque as dq


def bfs():
    while 1:
        p, n = q.popleft()

        if p == m:
            return n

        if p*2 < len(arr) and arr[p*2]:
            arr[p*2] = False
            q.append([p*2, n+1])
        if p+1 < len(arr) and arr[p+1]:
            arr[p+1] = False
            q.append([p+1, n+1])
        if p-1 >= 0 and arr[p-1]:
            arr[p-1] = False
            q.append([p-1, n+1])


if __name__ == "__main__":
    q = dq()
    n, m = map(int, input().split())

    arr = [True] * (max(n, m)*2+1)

    arr[n] = False
    q.append([n, 0])
    print(bfs())
