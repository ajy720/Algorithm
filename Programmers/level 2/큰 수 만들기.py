from collections import deque

def solution(number, k):
    answer = []

    number = deque(number)
    answer.append(number.popleft())

    while number and k > 0:
        while answer and k > 0 and answer[-1] < number[0]:
            k -= 1
            answer.pop(-1)
            
        answer.append(number.popleft())

    answer += list(number)

    if k:
        answer = answer[:-k]

    return ''.join(answer)


if __name__ == "__main__":
    # print(solution("1924", 2), "94")
    # print(solution("1231234", 3), "3234")
    print(solution("4177252841", 4), "775841")
    print(solution("11111111", 3), "11111")