if __name__ == "__main__":
    T, total_t, copy_t = map(int, input().split())

    for _ in range(T):
        arr = list(map(int, input().split()))
        n, arr = arr[0], arr[1:]
        dest = 0
        for i in range(n):
            dest += arr[i]
            if dest >= total_t:
                break
        
        idx = arr.index(max(arr[: i + 1]))
        arr[idx] = min(arr[idx], copy_t)
        # print(arr)

        dest = 0
        ans = 0
        for i in range(n):
            dest += arr[i]
            if dest > total_t:
                break
            else:
                ans += 1

        print(ans)
