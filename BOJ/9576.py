import sys

input = sys.stdin.readline

for _ in ' '*int(input()):
    n, m = map(int, input().split())

    arr = [[*map(int, input().split())] for _ in ' '*m]
    arr.sort(key=lambda x : x[1])
    books = [False] * (n+1)
    ans = 0

    for a, b in arr:
        for j in range(a, b+1):
            if not books[j]:
                books[j] = True
                ans += 1 
                break
            
    print(ans)