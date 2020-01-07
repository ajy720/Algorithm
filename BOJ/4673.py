def d(n:int) -> int:
    sum = n
    while n != 0:
        sum += n%10
        n //=10
    if sum > 10000:
        return
    print(sum)
    
    d(sum)

d(1)