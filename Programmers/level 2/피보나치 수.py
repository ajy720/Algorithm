def solution(n):
    dp = [1, 1]

    for i in range(2, n):
        dp.append((dp[-1]+dp[-2])%1234567)
    
    return dp[-1]


if __name__ == "__main__":
    print(solution(3), 2)
    print(solution(5), 5)
