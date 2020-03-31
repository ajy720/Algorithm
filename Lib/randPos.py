import random

def randPos(n, m):
    return [(random.randrange(n), random.randrange(n)) for _ in range(m)]

n, m = map(int, input().split())
val = randPos(n, m)
for i in val:
    print(*i)