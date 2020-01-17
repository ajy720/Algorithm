n, k = map(int, input().split())

arr = []

for _ in range(n):
    arr.insert(0, int(input()))

cnt = 0

for i in arr:
    cnt += k//i
    k %= i
    if k == 0:
        print(cnt)
        exit()