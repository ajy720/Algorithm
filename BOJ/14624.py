n = int(input())

if n%2 == 0:
    print("I LOVE CBNU")

else:
    print("*"*n)
    for i in range(n//2+1):
        print(" "*(n//2-i), end="")
        print("*", end="")
        if i > 0:
            print(" "*(i*2-1), end="")
            print("*", end="")
        print()
