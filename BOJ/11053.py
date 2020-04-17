n = int(input())

arr = list(map(int, input().split()))
ans = [1] * n

for i in range(n):
    try:
        ans[i] = max([ans[j] for j in range(0, i) if arr[j] < arr[i]]) + 1
    except:
        continue

print(max(ans))