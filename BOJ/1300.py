if __name__ == "__main__":
    n = int(input())
    k = int(input())

    left = 1
    right = k

    while left <= right:
        mid = (left + right)//2
        cnt = n * (mid//n) # i행 까지의 최대값은 i*j이니까, mid보다 작은 것들은 검사하지 않고 카운트

        for i in range(mid//n+1, n+1): # 검사 안 한 부분만 반복 검사
            cnt += mid//i # 

        if cnt < k:
            left = mid + 1
        else:
            right = mid - 1
            ans = mid
    
    print(ans)