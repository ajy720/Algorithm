import heapq


def solution(prices):
    answer = [0] * len(prices)

    q = []

    for i in range(len(prices)):
        heapq.heappush(q, [-prices[i], i])

        while abs(q[0][0]) > prices[i]:
            price, idx = heapq.heappop(q)
            price = abs(price)

            answer[idx] = i - idx
    
    while q:
        price, idx = heapq.heappop(q)
        answer[idx] = len(prices) - 1 - idx

    return answer


if __name__ == "__main__":
    prices = [1, 2, 3, 2, 3]

    print(solution(prices))
