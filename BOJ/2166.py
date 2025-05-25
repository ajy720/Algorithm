if __name__ == "__main__":
    n = int(input())
    arr = [tuple(map(int, input().split())) for _ in range(n)]
    ans = 0

    for i in range(n):
        A = arr[i]
        B = arr[(i + 1) % n]

        ans += A[0] * B[1] - B[0] * A[1]
    print(round(abs(ans) / 2, 1))
