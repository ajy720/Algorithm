n = int(input())

for i in range(n):
    print("*"*(i+1), end="")
    print(" "*((n-1-i)*2), end="")
    print("*"*(i+1))

for i in range(n-1, 0, -1):
    print("*"*i, end="")
    print(" "*((n-i)*2), end="")
    print("*"*i)