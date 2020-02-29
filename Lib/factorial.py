def factorial(n):
    ret = 1    
    for i in range(2, n+1): ret *= i
    return ret

if __name__ == "__main__":
    n = int(input())

    fact = factorial(n)

    print(fact)