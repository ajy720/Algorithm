lang = {
    'cpp': set(),
    'python': set(),
    'java': set()
}

position = {
    'backend': set(),
    'frontend': set()
}

career = {
    'junior': set(),
    'senior': set()
}

food = {
    'chicken': set(),
    'pizza': set()
}


def solution(info, query):
    answer = []

    base = set()

    for i in range(len(info)):
        info[i] = info[i].split()

        lang[info[i][0]].add(i)
        position[info[i][1]].add(i)
        career[info[i][2]].add(i)
        food[info[i][3]].add(i)

        info[i] = int(info[i][-1])
        base.add(i)

    for i in range(len(query)):
        query[i] = query[i].replace('and', '').split()
        query[i][-1] = int(query[i][-1])

        s = base.copy()

        if query[i][0] != '-':
            s = s.intersection(lang[query[i][0]])
        if query[i][1] != '-':
            s = s.intersection(position[query[i][1]])
        if query[i][2] != '-':
            s = s.intersection(career[query[i][2]])
        if query[i][3] != '-':
            s = s.intersection(food[query[i][3]])

        answer.append(len([no for no in s if info[no] >= query[i][-1]]))

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
