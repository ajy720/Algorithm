import sys

input = sys.stdin.readline

n = int(input())
ans = 0
arr = []
for _ in range(n):
    start, end = map(int, input().split())
    arr.append([end, start])

arr.sort()
start = [arr[i][1] for i in (range(len(arr)))]
end = [arr[i][0] for i in (range(len(arr)))]

i = 0
now = 0

while i < n:
    try:
        while start[i] < now:
            i += 1
    except:
        break
    ans += 1
    now = end[i]
    i += 1

print(ans)