arr = list(input())

ans = 0

a = abs(ord("A") - ord(arr[0]))
b = abs(a-26)

ans += a if a < b else b

for i in range(1, len(arr)):
    
    a = abs(ord(arr[i-1]) - ord(arr[i]))
    b = abs(a-26)

    ans += a if a < b else b

print(ans)