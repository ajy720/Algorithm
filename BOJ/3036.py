def getFactor(n, f:list):
    for i in range(2, int(n**(1/2))+1):
        if n % i == 0: 
            return getFactor(n//i, f+[i])

    if n == 1:
        return f
    
    return f + [n]

n = int(input())
arr = list(map(int, input().split()))

for i in arr[1:]:
    first = getFactor(arr[0], [])
    mom = 1
    for j in first:
        if i % j == 0:
            i //= j
        else:
            mom *= j
    
    print(f"{mom}/{i}")