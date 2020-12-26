def solution(progresses, speeds):
    answer = []

    while progresses:

        for i in range(len(progresses)):
            progresses[i] += speeds[i]

        if progresses[0] >= 100:
            i = 0
            for progress in progresses:
                if progress >= 100:
                    i += 1
                else:
                    break

            answer.append(i)
            progresses = progresses[i:]
            speeds = speeds[i:]

    return answer


if __name__ == "__main__":
    progresses = [93, 30, 55]
    speeds = [1, 30, 5]
    print(solution(progresses, speeds))

    progresses = [95, 90, 99, 99, 80, 99]
    speeds = [1, 1, 1, 1, 1, 1]
    print(solution(progresses, speeds))
