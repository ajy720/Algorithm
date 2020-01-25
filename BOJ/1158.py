n, k = map(int, input().split())

arr = [i for i in range(n)]
index = 0

print("<", end='')
while len(arr) > 1:
    index = (index + k-1) % len(arr)
    print(f"{arr.pop(index)+1}, ", end="")
print(arr[0]+1, ">", sep="")
