n = int(input())

arr = [*map(int, input().split())]
ans = [0] * n

for i in range(n):
    ans[arr[i]-1] = (arr[i]-1) - i

print(*ans, sep='\n')
