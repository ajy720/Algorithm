input()
arr = [*map(int, input().split())]
ans = 0
t = 0
for i in range(1, len(arr)):
    if arr[i] < arr[i-t-1]:
        t += 1
    else:
        ans = max(ans, t)
        t = 0
    
print(max(ans, t))