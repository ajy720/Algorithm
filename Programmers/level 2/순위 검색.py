from bisect import bisect_left

d = dict()


def solution(info, query):
    answer = []

    for i in range(len(info)):
        info[i] = info[i].split()
        info[i][-1] = int(info[i][-1])

        for o in range(16, 32):
            key = ''

            for idx, j in enumerate(f'{o:b}'[1:]):
                if j == '1':
                    key += info[i][idx]
                else:
                    key += '-'

            if key in d.keys():
                d[key].append(info[i][-1])
            else:
                d[key] = [info[i][-1]]

    for scores in d.values():
        scores.sort()

    for i in range(len(query)):
        query[i] = query[i].replace(' and ', '').split()
        query[i][-1] = int(query[i][-1])

        key = ''.join(query[i][:-1])
        t = 0

        try:
            scores = d[key]
            t = len(scores) - bisect_left(scores, query[i][-1])
        except:
            t = 0

        answer.append(t)

    return answer


if __name__ == "__main__":
    info = ["java backend junior pizza 150",
            "python frontend senior chicken 210",
            "python frontend senior chicken 150",
            "cpp backend senior pizza 260",
            "java backend junior chicken 80",
            "python backend senior chicken 50"]

    query = ["java and backend and junior and pizza 100",
             "python and frontend and senior and chicken 200",
             "cpp and - and senior and pizza 250",
             "- and backend and senior and - 150",
             "- and - and - and chicken 100",
             "- and - and - and - 150"]

    print(solution(info, query))
