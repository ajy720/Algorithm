inputs = []
while 1:
    n = int(input())
    if n != 0:
        inputs.append(n)
    else:
        break

n = max(inputs)
cnt = 0
num = [False, False] + [True]*(2*n)
for i in range(2, 2*n+1):
    if num[i]:
        for j in range(i*2, 2*n+1, i):
            num[j] = False

for n in inputs:
    print(num[n+1:2*n+1].count(True))