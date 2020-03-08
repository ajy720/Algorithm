import sys

input = sys.stdin.readline

white = 0
blue = 0

def solve(arr:list, n:int):
    global white, blue
    if n == 1:
        if arr[0][0]:
            blue += 1
            return True
        else:
            white += 1
            return False
    
    a = solve([i[:n//2] for i in arr[:n//2]], n//2)
    b = solve([i[n//2:] for i in arr[:n//2]], n//2)
    c = solve([i[:n//2] for i in arr[n//2:]], n//2)
    d = solve([i[n//2:] for i in arr[n//2:]], n//2)

    if a == b == c == d and a+b+c+d != -4:
        if arr[0][0]:
            blue -= 3
            return True
        else: 
            white -= 3
            return False
    
    else: return -1

if __name__ == "__main__":
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]

    solve(arr, n)

    print(white)
    print(blue)