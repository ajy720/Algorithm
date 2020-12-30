from collections import deque


def solution(priorities, location):
    answer = 0
    n = len(priorities)

    dq = deque()

    for i in range(n):
        dq.append((priorities[i], i))

    while dq:
        t = dq.popleft()

        if not dq:
            break            

        if t[0] >= max(dq)[0]:
            answer += 1
            if location == t[1]:
                return answer

            continue

        else:
            dq.append(t)

    return n


if __name__ == "__main__":
    priorities = [2, 1, 3, 2]
    location = 2
    print(solution(priorities, location))

    priorities = [1, 1, 9, 1, 1, 1]
    location = 0
    print(solution(priorities, location))
