def hanoi(start:int, end:int, n:int):
    if n == 1:
        print(start, end)
        return

    wp = 6-(start+end)
    hanoi(start, wp, n-1)

    print(start, end)

    hanoi(wp, end, n-1)

n = int(input())

print(2**n-1)

hanoi(1, 3, n)