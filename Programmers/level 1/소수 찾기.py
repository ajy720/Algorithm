def solution(n):
    answer = 0

    primeN = [True] * (n+1)
    primeN[0] = primeN[1] = False

    for i in range(2, n + 1):
        if primeN[i]:
            for j in range(i*2, n+1, i):
                primeN[j] = False
            
            answer += 1
    
    return answer


if __name__ == "__main__":
    print(solution(10))
    print(solution(5))
