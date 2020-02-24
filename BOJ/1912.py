n  = int(input())
arr = [0] + list(map(int, input().split()))

for i in range(1, n+1):
    arr[i] = max(arr[i], arr[i-1] + arr[i])

print(max(arr[1:]))