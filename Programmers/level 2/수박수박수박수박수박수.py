def solution(n):
    answer = '수박'
    answer *= n//2
    if n%2 == 1:
        answer += '수'

    return answer


if __name__ == "__main__":
    # print(solution(3))
    # print(solution(4))
    print(solution(5))

