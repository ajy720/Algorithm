import sys

def lower_bound(k):
    left = 0
    right = len(arr)
     
    while left < right:
        mid = (left+right)//2
     
        if arr[mid] < k: left = mid + 1
        else: right = mid
    
    return right

if __name__ == "__main__":
    n = int(input())
    arr = []
    for _ in range(n):
        o = int(sys.stdin.readline())
        if o == 0:
            try: print(arr.pop(-1))
            except: print(0)
        else:
            arr.insert(lower_bound(o), o)