def solution(A: list, B: list):
    answer = 0

    A.sort()
    B.sort(reverse=True)

    for a in A:
        while B:
            if a < B.pop():
                answer += 1
                break

    return answer


if __name__ == "__main__":
    # print(solution([5, 1, 3, 7], [2, 2, 6, 8]))
    # print(solution([2, 2, 2, 2], [1, 1, 1, 1]))
    # print(solution([2, 3, 4, 5, 6, 7], [7, 6, 5, 4, 3, 2]))
    print(solution([*map(int, input().split())], [*map(int, input().split())]))
