def solve(m:int, bt:list):
    if m == 0:
        for i in bt: print(i, end=" ")
        print()
        return
        
    for i in range(bt[-1] if bt else 1, n+1):
        if i not in bt:
            solve(m-1, bt+[i])

n, m = map(int, input().split())

solve(m, [])