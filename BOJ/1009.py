n = int(input())

for i in range(n):
    a, b = map(int, input().split())
    res = a
    b = b % 4 + 4

    for j in range(2, b+1):
        res = res * a % 10

    if res == 0:
        res = 10
    
    print(res)