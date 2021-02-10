def solution(routes: list):
    answer = 1

    routes.sort()

    tmp = 30001

    for start, end in routes:
        if start > tmp:
            tmp = end
            answer += 1
        if end < tmp:
            tmp = end

    return answer


if __name__ == "__main__":
    print(solution([[-20, 15], [-14, -5], [-18, -13], [-5, -3]]))
    print(solution([[-2, -1], [1, 2], [-3, 0]]))
    print(solution([[0, 0]]))
    print(solution([[0, 1], [0, 1], [1, 2]]))
    print(solution([[0, 1], [2, 3], [4, 5], [6, 7]]))
    print(solution([[-20, 15], [-14, -5], [-18, -13], [-5, -3]]))
    print(solution([[-20, 15], [-20, -15], [-14, -5], [-18, -13], [-5, -3]]))
