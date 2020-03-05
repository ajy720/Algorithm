from collections import deque

n, k = map(int, input().split())
q = deque([i for i in range(1, n+1)])

print("<", end='')
while 1:
    q.rotate(-(k-1))
    print(q.popleft(), end='')
    if q: print(", ", end='')
    else: break

print(">", end='')