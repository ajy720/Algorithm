n = int(input())

for i in range(n):
    print(" "*i, end="")
    print("*"*((n-i)*2-1))

for i in range(n-1, 0, -1):
    print(" "*(i-1), end="")
    print("*"*((n-i+1)*2-1))