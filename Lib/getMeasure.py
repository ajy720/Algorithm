def getMeasure(n:int):
    f = []
    sq = int(n**(1/2))
    for i in range(2, sq):
        if n % i == 0:
          f[len(f)//2-1:len(f)//2] += [i, n//i]

    if n % sq == 0:
        f.insert(len(f)//2, sq)

    return f + [n]

if __name__ == "__main__":
    n = int(input())

    measure = getMeasure(n)

    print(measure)