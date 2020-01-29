n = int(input())+1

arr = list(map(int, input().split()))

arr.sort()

print(arr[n//2-1])