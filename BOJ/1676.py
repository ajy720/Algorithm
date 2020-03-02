def factorial(n):
    ret = 1    
    for i in range(2, n+1): ret *= i
    return ret

if __name__ == "__main__":
    n = int(input())

    fact = factorial(n)
    ans = 0
    while fact % 10 == 0:
        ans += 1
        fact//=10
        
    print(ans)