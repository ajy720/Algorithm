from math import sqrt


def solution(n):
    answer = 0

    t = int(sqrt(n))
    if t**2 == n:
        answer = (t+1)**2
    else:
        answer = -1

    return answer


if __name__ == "__main__":
    n = int(input())
    print(solution(n))
