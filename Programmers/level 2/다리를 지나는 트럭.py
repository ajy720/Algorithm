from collections import deque


def solution(bridge_length, weight, truck_weights):
    n = len(truck_weights)

    truck_weights = deque(truck_weights)
    passing = deque([])

    answer = 0
    s = 0
    while truck_weights or passing:
        if passing and bridge_length - (answer - passing[0][1]) <= 0:
            s -= passing.popleft()[0]

        if truck_weights and s + truck_weights[0] <= weight:
            s += truck_weights[0]
            passing.append([truck_weights.popleft(), answer])
        answer += 1

    return answer


if __name__ == "__main__":

    bridge_length = 2
    weight = 10
    truck_weights = [7, 4, 5, 6]
    print(solution(bridge_length, weight, truck_weights))

    bridge_length = 100
    weight = 100
    truck_weights = [10]
    print(solution(bridge_length, weight, truck_weights))

    bridge_length = 100
    weight = 100
    truck_weights = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
    print(solution(bridge_length, weight, truck_weights))
