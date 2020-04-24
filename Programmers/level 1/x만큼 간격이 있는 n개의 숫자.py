def solution(n):
    answer = 0
    arr = []
    while n:
        arr.append(n%10)
        n //= 10

    for i in sorted(arr, reverse=True):
        answer *= 10
        answer += i

    return answer