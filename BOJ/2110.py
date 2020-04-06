import sys

if __name__ == "__main__":
    n, c = map(int, input().split())

    arr = sorted([int(i) for i in sys.stdin])

    l = 1
    r = arr[-1] - arr[0]

    while l <= r:
        mid = (l + r)//2
        idx, cnt = 0, 1

        for i in range(1, n):
            if arr[i] - arr[idx] >= mid:
                cnt+=1
                idx = i
            else: 
                continue

            if cnt >= c: break
        
        if cnt >= c: 
            ans = mid
            l = mid + 1
        else: 
            r = mid - 1

    print(ans)