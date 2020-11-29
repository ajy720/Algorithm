if __name__ == "__main__":
    n = int(input())

    arr = [False] * (n+1)
    cnt = 0
    ans = 0

    for i in [*map(int, input().split())]:
        if arr[i]:
            cnt -= 1
        else:
            arr[i] = True
            cnt += 1
            ans = max(ans, cnt)
    
    print(ans)
    