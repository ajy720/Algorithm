def getMeasure(n:int):
    f = []
    sq = int(n**(1/2))
    for i in range(2, sq+1):
        if n % i == 0:
            if n//i == sq: f.insert(len(f)//2, sq)
            else: f[len(f)//2-1:len(f)//2] += [i, n//i]

    return f + [n]

if __name__ == "__main__":
    n = int(input())

    measure = getMeasure(n)

    print(measure)