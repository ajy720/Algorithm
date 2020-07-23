cnt = 0

def solve(bt, p, n):
    global cnt
    if len(bt) == n:
        if sum(bt) == s:
            cnt += 1
    
    else:
        for i in range(p, len(arr)):
            solve(bt + [arr[i]], i+1, n)



if __name__ == "__main__":
    n, s = map(int, input().split())
    arr = [*map(int, input().split())]

    for i in range(n):
        solve([], 0, i+1)

    print(cnt)

