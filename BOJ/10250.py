for _ in range(int(input())):
    h, w, n = map(int, input().split())

    print("%d%02d"%(n%h if n%h != 0 else h, n//h+1 if n%h != 0 else n//h))