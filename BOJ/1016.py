from math import sqrt
from math import ceil
from math import floor

min, max = map(int, input().split())

num = []
res = [False]*(max-min+1)

MAX = int(sqrt(max))
filt = [False, False] + [True]*(MAX-1)
for i in range(2, MAX+1):
    if filt[i]:
        num.append(i**2)
        for j in range(i*2, MAX+1, i):
            filt[j] = False

for i in num:
    #floor(max/i) - ceil(min/i) + 1 : max와 min 사이에 i의 배수가 몇 개 있는지 구하는 식.
    for j in range(ceil(min/i), floor(max/i)+1):
        res[i*j-min] = True

print(res.count(False))