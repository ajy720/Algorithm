def f(n:int):
    global zero
    global one
    if n == 0:
        zero += 1
    elif n == 1:
        one += 1
    else:
        
        if fibo[n] != 0: 
            zero += fibo[n][0]
            one += fibo[n][1]
            return

        f(n-1)
        f(n-2)
        fibo[n] = (zero, one)

for _ in range(int(input())):    
    zero = 0
    one = 0
    fibo = [0]*41

    f(int(input()))

    print(zero, one)