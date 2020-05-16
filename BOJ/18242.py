n, m = map(int, input().split())
ans = 1
arr = []
cnt = []

for i in range(n):
    arr.append(input())

for i in range(n):
    if arr[i].count('#') == 1:
        ans = 2

if ans == 1:
    cnt = [arr[i].count('#') for i in range(n)]
    if cnt.index(max(cnt)) > cnt.index(max(cnt)-1):
        print("UP")
        exit()
    else:
        print("DOWN")
        exit()
else:
    for i in range(m):
        cnt.append([arr[j][i] for j in range(n)].count('#'))

    if cnt.index(max(cnt)) > cnt.index(max(cnt)-1):
        print("LEFT")
        exit()
    else:
        print("RIGHT")
        exit()