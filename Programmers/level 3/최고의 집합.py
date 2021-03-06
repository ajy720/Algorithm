def solution(n, s):
    answer = []

    t = s // n
    r = s % n

    if n > s:
        return [-1]

    for i in range(n):
        c = t
        if r:
            r -= 1
            c += 1

        s -= c
        answer.append(c)

    answer.sort()

    return answer

if __name__ == "__main__":
    print(solution(2, 9))
    print(solution(2, 1))
    print(solution(2, 8))
    print(solution(3, 11))
    print(solution(4, 15))