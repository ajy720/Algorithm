from itertools import accumulate, combinations


def solution(orders: list, course: list):
    answer = []
    courses = [dict() for _ in ' '*11]

    for t in course:
        for order in orders:
            if len(order) < t:
                continue

            for comb in combinations(order, t):
                comb = ''.join(sorted(comb))

                if comb in courses[t]:
                    courses[t][comb] += 1
                else:
                    courses[t][comb] = 1

        if not courses[t]:
            continue

        courses[t] = sorted(courses[t].items(),
                            key=lambda x: x[1], reverse=True)

        mCnt = courses[t][0][1]

        if mCnt < 2:
            continue

        for course, cnt in courses[t]:
            if cnt < mCnt:
                break
            else:
                answer.append(course)

    return sorted(answer)


if __name__ == '__main__':
    print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2, 3, 4]))

    print(solution(["ABCDE", "AB", "CD", "ADE",
                    "XYZ", "XYZ", "ACD"], [2, 3, 5]))

    print(solution(["XYZ", "XWY", "WXA"], [2, 3, 4]))
