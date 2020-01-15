m, n = map(int, input().split())

prime = []
num = [False, False] + [True]*n
for i in range(2, n+1):
    if num[i]:
        if i >= m:
            print(i)
        for j in range(i*2, n+1, i):
            num[j] = False