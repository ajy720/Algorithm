for _ in range(int(input())):
    n,m=map(int,input().split())
    s=m*11+4 
    if s>n*m or m<4: print(-1)
    else: print(s)