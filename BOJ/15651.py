def solve(m:int, bt:list):
    if m == 0:
        print(' '.join(bt))
        return

    for i in range(1, n+1):
        solve(m-1, bt+[str(i)])

n, m = map(int, input().split())

solve(m, [])