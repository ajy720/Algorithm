a = int(input())
b = int(input())
c = int(input())

n = str(a*b*c)
numlist = [0]*10
del a, b ,c

for i in n:
    numlist[int(i)] += 1

for i in numlist:
    print(i)