import sys

dp = []


def solution(n, number):
    global dp

    answer = 0

    dp = [sys.maxsize] * (number * n + 1)
    dp[0] = 2
    dp[1] = 2
    dp[n] = 1

    for j in range(1, 6):
        if int(str(n)*j) > number * n:
            break

        dp[int(str(n)*j)] = j

    for i in range(2, len(dp)):
        for j in range(1, i):
            if j >= number:
                break
            
            a = max(i, j)
            b = min(i, j)

            t = dp[a] + dp[b]

            if not a+b >= len(dp):
                dp[a+b] = min(dp[a+b], t)
            dp[a-b] = min(dp[a-b], t)
            if not a*b >= len(dp):
                dp[a*b] = min(dp[a*b], t)
            dp[a//b] = min(dp[a//b], t)

    answer = -1 if dp[number] > 8 else dp[number]

    return answer


if __name__ == "__main__":
    n = 5
    number = 12
    print(solution(n, number))

    n = 2
    number = 11
    print(solution(n, number))

    n = 1
    number = 1121
    print(solution(n, number))


if __name__ == "__main__":
    n = 5
    number = 12
    print(solution(n, number))

    n = 2
    number = 11
    print(solution(n, number))

    n = 1
    number = 5
    print(solution(n, number))
