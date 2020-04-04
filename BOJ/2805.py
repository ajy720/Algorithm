if __name__ == "__main__":
    n, m = map(int, input().split())

    arr = sorted([*map(int, input().split())])

    left = 0
    right = arr[-1]

    while 1:
        mid = (left + right)//2
        cnt = 0
        flag = True

        if mid == left or mid == right: break

        for i in range(len(arr)):
            if arr[i]-mid > 0: 
                idx = i
                break

        for i in arr[idx:]: cnt += i - mid

        if cnt >= m: 
            left = mid
            arr = arr[idx:]
        else: 
            right = mid
            
    print(mid)