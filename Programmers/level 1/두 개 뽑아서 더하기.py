from itertools import combinations

def solution(numbers):
    answer = []

    arr = [*map(sum, combinations(numbers, 2))]

    answer = sorted(set(arr))

    return answer

if __name__ == "__main__":
    numbers = [2,1,3,4,1]
    print(solution(numbers))

    numbers = [5,0,2,7]
    print(solution(numbers))

