def solution(n):
    answer = []

    arr = [[0]*i for i in range(1, n+1)]
    arr[0][0] = 1

    x = 0
    y = 0
    cnt = 1

    while 1:
        if cnt == (n+1) * n // 2:
            break

        # 1. 아래로 내려가는 스텝
        while 1:
            if y + 1 >= n or arr[y+1][x]:
                break

            y += 1
            cnt += 1
            arr[y][x] = cnt


        # 2. 오른쪽으로 가는 스텝
        while 1:
            if x + 1 >= len(arr[y]) or arr[y][x+1]:
                break

            x += 1
            cnt += 1
            arr[y][x] = cnt


        # 3. 좌상향으로 가는 스텝
        while 1:
            if arr[y-1][x-1]:
                break

            y -= 1
            x -= 1
            cnt += 1

            arr[y][x] = cnt

    for i in arr:
        answer += i

    return answer


if __name__ == "__main__":
    n = 4
    print(solution(n))

    n = 5
    print(solution(n))

    n = 6
    print(solution(n))
