s1 = input()
s2 = input()
ans = 0
arr = [[0] * (len(s2)+1) for i in range(len(s1)+1)]

for i in range(1, len(s1)+1):
    for j in range(1, len(s2)+1):
        try:
            if s1[i-1] == s2[j-1]:
                arr[i][j] = arr[i-1][j-1] + 1 
                ans = max(arr[i][j], ans)
            else:
                arr[i][j] = max(arr[i-1][j], arr[i][j-1])
        except:
            arr[i][j] = 0

print(ans)