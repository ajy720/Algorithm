n = int(input())
arr = [[0, 0, 0, 0] for i in range(n+2)]

for i in range(1, n+1):
    arr[i][0] = arr[i][1] = arr[i][2] = arr[i][3] = int(input())

for i in range(1, n+1):
    arr[i][0] += max(arr[i-2][0], arr[i-2][1], arr[i-1][2])
    arr[i][1] += max(arr[i-1][0], arr[i-1][2])
    arr[i][2] = max(arr[i-1])

print(max(max(arr[n]), max(arr[n-1])))