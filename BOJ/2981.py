def getMeasure(n:int):
    f = []
    sq = int(n**(1/2))
    for i in range(2, sq+1):
        if n % i == 0:
            if n//i == sq: f.insert(len(f)//2, sq)
            else: f[len(f)//2-1:len(f)//2] += [i, n//i]

    return f + [n]

n = int(input())
ans = ""
arr = sorted([int(input()) for i in range(n)])

for i in getMeasure(arr[1]-arr[0]):
    res = arr[0] % i
    for j in arr[1:]:
        if j % i != res: 
            res = j % i
            break
    if res == arr[0] % i:
        ans += str(i)+" "

print(ans[:-1])