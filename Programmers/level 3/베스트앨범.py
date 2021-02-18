def solution(genres: list, plays: list):
    answer = []
    d = {}
    for i in range(len(genres)):
        if genres[i] in d:
            d[genres[i]][0] += plays[i]
        else:
            d[genres[i]] = [plays[i]]

        d[genres[i]].append((plays[i], -i))

    d = sorted(d.values(), reverse=True)
    print(d)

    for genre in d:
        genre = sorted(genre[1:], reverse=True)

        print(genre)
        answer += map(lambda x: -x[1], genre[:2])

    return answer


# genres = ["c", "p", "c", "c", "p", 'd']
# plays = [500, 2501, 150, 800, 2500, 12]

genres = input().split()
plays = [*map(int, input().split())]

print(solution(genres, plays))
