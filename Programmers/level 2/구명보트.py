from collections import deque

def solution(people, limit):
    answer = 0
    people.sort(reverse=True)

    people = deque(people)

    while people:
        if len(people) > 1 and people[0] + people[-1] <= limit:
            people.pop()
            people.popleft()
        else:
            people.popleft()
        
        answer += 1

    return answer


if __name__ == "__main__":
    print(solution([70, 50, 80, 50], 100))
    print(solution([70, 80, 50], 100))

