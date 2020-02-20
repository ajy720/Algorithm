import sys

input = sys.stdin.readline

n = int(input())

arr = list(map(int, input().split()))
ans = [[1, 1] for i in range(n)] # ans[x][0]은 증가수열, ans[x][1]은 감소수열

for i in range(n):
    try:
        ans[i][0] = max([ans[j][0] for j in range(i) if arr[j] < arr[i]]) + 1
    except:
        pass
    try:
        ans[i][1] = max(max([ans[j][1] for j in range(i) if arr[j] > arr[i]]) + 1, max([ans[j][0] for j in range(i) if arr[j] > arr[i]]) + 1)
    except:
        continue

print(max(max([ans[i][0] for i in range(n)]),max([ans[i][1] for i in range(n)])))