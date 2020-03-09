import sys

input = sys.stdin.readline

def prevent(arr):
    for i in arr:
        for j in i:
            if arr[0][0] != j: return False

    return True

def solve(arr:list, n:int):
    if prevent(arr):
        ans[arr[0][0]] += 1
        return
        
    m = n//3
    for i in range(0, n, m):
        for j in range(0, n, m):
            solve([i[j:j+(m)] for i in arr[i:i+(m)]], m)

if __name__ == "__main__":
    n = int(input())

    arr = [[*map(int, i.split())] for i in sys.stdin]

    ans = [0, 0, 0]
    solve(arr, n)
    print(f'{ans[-1]}\n{ans[0]}\n{ans[1]}')