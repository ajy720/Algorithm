from math import sqrt


def solution(n):
    answer = 0

    for i in range(1, int(sqrt(n))+1):
        if n % i:
            continue
        else:
            answer += i + ((n // i) if i != n // i else 0)

    return answer


if __name__ == "__main__":
    print(solution(int(input())))
