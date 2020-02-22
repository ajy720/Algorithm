import sys

maxv = sys.maxsize * -1

n = int(input())

arr = [[0, 0, 0] for i in range(n+1)]

for i in range(n):
    arr[i][0] = arr[i][1] = arr[i][2] = int(input())

arr[1][1] += arr[0][0]
for i in range(2, n):
    arr[i][0] += max(arr[i-2][0], arr[i-2][1])
    arr[i][1] += arr[i-1][0]

print(max(arr[n-1]))