from functools import reduce

STONE = 100

if __name__ == "__main__":
    p = int(input())
    n = int(input())
    arr = [0] * STONE

    for _ in ' '*n:
        pos, d = input().split()
        pos = int(pos) - 1

        if d == 'R':
            for i in range(pos+1, STONE):
                arr[i] += 1

        elif d == 'L':
            for i in range(0, pos):
                arr[i] += 1

    for i in range(STONE):
        arr[i] %= 3

    for i in range(3):
        print("%.2f"%(p/STONE*arr.count(i)))


            
