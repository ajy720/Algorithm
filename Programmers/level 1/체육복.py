def solution(n, lost, reserve):
    answer = n

    for i in lost.copy():
        if i in reserve:
            reserve.remove(i)
            lost.remove(i)
        else:
            answer -= 1

    for i in lost:
        if i-1 in reserve:
            answer += 1
            reserve.remove(i-1)
            continue

        if i+1 in reserve:
            answer += 1
            reserve.remove(i+1)
            continue

    return answer


if __name__ == "__main__":
    # n = 5
    # lost = [1, 2, 3, 4, 5]
    # reserve = [1, 3, 5]
    # print(solution(n, lost, reserve))

    # n = 5
    # lost = [2, 4]
    # reserve = [1, 3, 5]
    # print(solution(n, lost, reserve))

    # n = 5
    # lost = [2, 4]
    # reserve = [3]
    # print(solution(n, lost, reserve))

    # n = 3
    # lost = [3]
    # reserve = [1]
    # print(solution(n, lost, reserve))

    n = 5
    lost = [1, 2, 4, 5]
    reserve = [2, 3, 4]
    print(solution(n, lost, reserve))

    # n = int(input())
    # lost = [*map(int, input().split())]
    # reserve = [*map(int, input().split())]
    # print(solution(n, lost, reserve))
