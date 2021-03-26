t = int(input())

arr = [input() for _ in ' '*t]

n = len(arr[0])

ans = []

for i in range(n):
    ans.append(arr[0][i])
    for j in range(1, t):
        if arr[j][i] != arr[j-1][i]:
            ans[-1] = "?"
            break

print(''.join(ans))
    
