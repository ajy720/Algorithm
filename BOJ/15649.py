def solve(m:int, bt:list):
    if m == 1:
        for i in range(1, n+1):
            if str(i) not in bt:
                if bt: print(' '.join(bt), i)
                else : print(i)
    
    for i in range(1, n+1):
        if str(i) not in bt:
            solve(m-1, bt+[str(i)])

n, m = map(int, input().split())

solve(m, list([]))