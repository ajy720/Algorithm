if __name__ == "__main__":
    n = int(input())
    k = int(input())

    left = 1
    right = k

    while left <= right:
        mid = (left + right)//2
        cnt = 0

        for i in range(n):
            cnt += min(mid//(i+1), n)

        if cnt < k:
            left = mid + 1
        else:
            right = mid - 1
            ans = mid
    
    print(ans)