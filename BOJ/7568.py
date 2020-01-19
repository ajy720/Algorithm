n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))


for i in arr:
    cnt = 0
    for j in arr:
        if i[0] < j[0] and i[1] < j[1]:
            cnt += 1
    print(cnt+1)

