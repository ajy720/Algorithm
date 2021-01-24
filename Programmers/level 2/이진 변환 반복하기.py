def solution(s):
    answer = [0, 0]

    while s != '1':
        t = s.count('0')
        answer[1] += t

        s = f'{len(s) - t:b}'      


        answer[0] += 1

    return answer


if __name__ == "__main__":
    print(solution("110010101001"))
    print(solution("01110"))
    print(solution("1111111"))
