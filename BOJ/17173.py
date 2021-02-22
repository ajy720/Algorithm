n, m = map(int, input().split())

arr = [*map(int, input().split())]

s = set()

for i in arr:
    for j in range(0, n+1, i):
        s.add(j)

print(sum(s))