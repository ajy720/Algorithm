def getFactor(n:int):
    f = []
    sq = int(n**(1/2))
    for i in range(2, sq+1):
        if n % i == 0:
            if n//i == sq: f.insert(len(f)//2, sq)
            else: f[len(f)//2-1:len(f)//2] += [i, n//i]

    return f + [n]

n = int(input())

arr = [set(getFactor(int(input()))) for i in range(n)]

s = arr[0]

for i in range(1, n):
    s = s & arr[i]

    if len(s) == 1:
        print(s)
        exit()
    
print(s)