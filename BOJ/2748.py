arr = [0, 1, 1]
n = int(input())

for i in range(3, n+1):
    arr.append(arr[i-1]+arr[i-2])

print(arr[n])