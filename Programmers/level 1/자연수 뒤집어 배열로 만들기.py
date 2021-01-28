def solution(n):
    answer = []

    while n:
        answer.append(n % 10)
        n //= 10

    return answer


if __name__ == "__main__":
    print(solution(int(input())))
