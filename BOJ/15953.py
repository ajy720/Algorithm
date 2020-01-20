price = [500, 300, 200, 50, 30, 10]

for _ in range(int(input())):
    a, b = map(int, input().split())

    if  0 < a < 22:    
        temp = 0
        for i in range(1, 7):
            temp += i
            if a <= temp: break
        a = price[i-1]*10000
    else: a = 0

    if 0 < b < 32:
        temp = 0
        for i in range(1, 6):
            temp = 2**i-1
            if b <= temp: break
        b = (2**(10-i))*10000
    else : b = 0

    print(a+b)

