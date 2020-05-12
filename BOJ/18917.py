import sys

input = sys.stdin.readline

sum = 0
xor = 0

n = int(input())
for _ in range(n):
    oper = input().strip()

    try: oper, o = oper.split()
    except: pass

    if oper == '1':
        o = int(o)
        sum += o
        xor ^= o
    elif oper == '2':
        o = int(o)
        sum -= o
        xor ^= o
    elif oper == '3':
        print(sum)
    elif oper == '4':
        print(xor)