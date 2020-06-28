
import sys

input = sys.stdin.readline

for _ in ' '*int(input()):
    n = int(input())
    temp = [n]
    while n != 1:
        if n % 2:
            n = n*3+1
        else:
            n//=2

        temp.append(n)
        
    print(max(temp))