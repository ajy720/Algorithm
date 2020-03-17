import sys

sys.setrecursionlimit(10**6)

def find(arr, start, end, n):
    if start == end and arr[start] != n: return False

    mid = (start + end)//2

    if arr[mid] == n: return mid+1
    elif arr[mid] > n: return find(arr, start, mid-1, n)
    elif arr[mid] < n: return find(arr, mid+1, end, n)

if __name__ == "__main__":
    n = int(input())

    arr = sorted([*map(int, input().split())])

    m = int(input())

    chk_arr = [*map(int, input().split())]

    for i in chk_arr:
        if find(arr, 0, len(arr)-1, i): print(1)
        else: print(0)