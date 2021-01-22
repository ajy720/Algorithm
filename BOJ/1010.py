def combination(n, m):
    n = min(n, m-n)
    
    mom = 1
    son = 1

    for i in range(n):
        mom *= m - i
        son *= i + 1

    return mom//son


for _ in range(int(input())):
    print(combination(*map(int, input().split())))
