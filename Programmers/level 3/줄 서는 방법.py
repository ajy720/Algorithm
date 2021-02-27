def solution(n, k):
    answer = []

    caseN = 1
    nums = [*range(1, n+1)]
    k -= 1

    for i in range(1, n+1):
        caseN *= i

    while k > 0:
        numIdx = k // (caseN // n)
        answer.append(nums.pop(numIdx))

        k %= (caseN // n)
        caseN //= n
        n -= 1

    answer.extend(nums)

    return answer


if __name__ == "__main__":
    n = 4
    caseN = 1
    for i in range(1, n+1):
        caseN *= i

    for i in range(1, caseN+1):
        print(solution(n, i))
