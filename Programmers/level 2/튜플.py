def solution(s):
    d = dict()

    s = s[1:-1]

    s = eval(s)

    if len(s) == 1:
        return list(s)

    answer = [0] * len(s)

    for i in s:
        for j in i:
            if j in d.keys():
                d[j] += 1
            else:
                d[j] = 1

    for key, value in zip(d.keys(), d.values()):
        answer[-value] = key

    return answer


if __name__ == "__main__":
    print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))
    print(solution("{{1,2,3},{2,1},{1,2,4,3},{2}}"))
    print(solution("{{20,111},{111}}"))
    print(solution("{{123}}"))
    print(solution("{{4,2,3},{3},{2,3,4,1},{2,3}}"))
