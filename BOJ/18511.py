n, k = input().split()
s = list(map(int, input().split()))

n = int(n)
while n > 0:
    t = n
    tarr = []
    while t > 0:
        tarr[0:0]=[t%10]
        t//=10

    flag = True
    for i in range(len(tarr)):
        if not tarr[i] in s:
            flag = False
            n -= n%10**(len(tarr)-i-1) + 1

    if flag: 
        print(n)
        break
'''
100000000 8
1 2 3 4 5 6 7 8

546 3
8 7 9

907 2
9 4

984054 3
4 5 6

657 3
1 5 7

657 3
6 7 8
'''