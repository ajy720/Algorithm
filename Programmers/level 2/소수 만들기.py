from itertools import combinations

def solution(nums: list):
    answer = 0

    nums.sort()
    m = sum(nums[-3:])

    primeN = [2]
    prime = [False] * (m+1)
    prime[2] = True

    for i in range(3, m+1):
        flag = True

        for j in primeN:
            if i % j == 0:
                flag = False
                break

        if flag:
            primeN.append(i)
            prime[i] = True

    for s in combinations(nums, 3):
        if prime[sum(s)]:
            answer += 1

    return answer


if __name__ == "__main__":
    print(solution([*map(int, input().split())]))
