from math import sqrt

for _ in range(int(input())):
    x = [0]*2
    y = [0]*2
    r = [0]*2
    x[0], y[0], r[0], x[1], y[1], r[1] = map(int, input().split())

    distance = (x[0]-x[1])**2+(y[0]-y[1])**2
    if distance == 0:
        if r[0] == r[1]:
            print(-1)
        else:
            print(0)
            
    elif distance > sum(r)**2 or distance < abs(r[0]-r[1])**2:
        print(0)
    elif distance == sum(r)**2 or abs(r[0]-r[1])**2 == distance:
        print(1)
    else:
        print(2)