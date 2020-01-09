import sys
sys.setrecursionlimit(10**6)

limit = 10001

num = [False]*limit

def d(n:int):
    sum = n
    while n != 0:
        sum += n%10
        n //=10

    if sum > limit-1:
        return
    num[sum]=True
    
    d(sum)


for i in range(1, limit):
    if num[i] == False:
        d(i)

for i in range(1, limit):
    if num[i] == False:
        print(i, end=' ')