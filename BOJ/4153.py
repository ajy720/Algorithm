n = [0]*3
while 1:
    n = list(map(int, input().split()))
    if n.count(0) == 3:
        break
    temp = max(n)
    n.remove(temp)
    if temp**2 == n[0]**2 + n[1]**2:
        print("right")
    else:
        print("wrong")