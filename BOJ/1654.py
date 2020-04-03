import sys

if __name__ == "__main__":
    k, n = map(int, input().split())

    arr = sorted([int(_) for _ in sys.stdin])
    
    left = 0
    right = arr[-1]

    while 1:
        cnt = 0
        mid = (left+right)//2
        if mid == left: 
            for i in arr: cnt += i//(mid+1)
            if cnt >= n: mid += 1
            break

        for i in arr:
            cnt += i//mid

        if cnt < n:
            right = mid
        elif cnt >= n:
            left = mid
            
    print(mid)