n = int(input())
arr = []

for _ in range(n):
    arr.append(int(input()))

for i in range(n):
    for j in range(i+1, n):
        if arr[i] > arr[j]:
            arr[i], arr[j] = arr[j], arr[i]

for i in arr:
    print(i)