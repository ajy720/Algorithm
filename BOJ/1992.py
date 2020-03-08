import sys

input = sys.stdin.readline

def solve(arr:list, n:int):
    if n == 1:
        if arr[0][0] == "1": return "1"
        else: return "0"

    a = solve([i[:n//2] for i in arr[:n//2]], n//2)
    b = solve([i[n//2:] for i in arr[:n//2]], n//2)
    c = solve([i[:n//2] for i in arr[n//2:]], n//2)
    d = solve([i[n//2:] for i in arr[n//2:]], n//2)

    if a == b == c == d and len(a+b+c+d) == 4:
        if arr[0][0] == "1": return "1"
        else: return "0"
    
    else: return "("+a+b+c+d+")"

if __name__ == "__main__":
    n = int(input())
    arr = [[c for c in input().rstrip("\n")] for _ in range(n)]

    print(solve(arr, n))