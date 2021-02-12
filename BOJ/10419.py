for _ in range(int(input())):
    n = int(input())

    for i in range(n//2, -1, -1):
        if i + i**2 <= n:
            print(i)
            break
