import sys
input = sys.stdin.readline

n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))
arr.sort()
arr = [arr[i][1] for i in range(n)]
ans = [1] * n
for i in range(n):
    try:
        ans[i] = max(ans[j] for j in range(i) if arr[j] < arr[i]) + 1
    except:
        continue

print(n - max(ans))