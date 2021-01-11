from heapq import heapify, heappop, heappush


def solution(scoville, K):
    answer = 0

    heapify(scoville)

    while scoville[0] < K:
        if (len(scoville) < 2 and scoville[0] < K):
            return -1

        a = heappop(scoville)
        b = heappop(scoville)

        answer += 1

        heappush(scoville, a + b * 2)

    return answer


if __name__ == "__main__":
    scoville = [1, 2, 3, 9, 10, 12]
    k = 7
    print(solution(scoville, k))

    scoville = [0, 1, 3, 9, 10, 12]
    k = 9
    print(solution(scoville, k))
