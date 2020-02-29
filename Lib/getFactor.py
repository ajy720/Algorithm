def getFactor(n, f:list):
    for i in range(2, int(n**(1/2))+1):
        if n % i == 0: 
            return getFactor(n//i, f+[i])

    if n == 1:
        return f
    
    return f + [n]

if __name__ == "__main__":
    n = int(input())

    factors = getFactor(n, [])

    print(factors)