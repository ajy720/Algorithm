def timestamp(time):

    time, pTime = time.split()[1:]

    ret = 0
    h, m, s = time.split(':')

    if pTime:
        pTime = int(float(pTime[:-1]) * 1000)

    ret += int(h) * 3600 * 1000
    ret += int(m) * 60 * 1000
    ret += int(float(s) * 1000)

    return ret - pTime + 1, ret


def solution(lines):
    answer = 0
    n = len(lines)
    stamp = [[0, 0] for _ in ' '*n]

    for i in range(n):
        stamp[i] = timestamp(lines[i])

    for i in range(n):
        start, end = stamp[i]
        startR = start + 999
        endR = end + 999

        cnt1 = []
        cnt2 = []

        for j in range(n):
            s, e = stamp[j]
            if not (startR < s or e < start):
                cnt1.append(j)

            if not (endR < s or e < end):
                cnt2.append(j)

        answer = max(answer, len(cnt1), len(cnt2))

    return answer


if __name__ == "__main__":
    lines = [
        "2016-09-15 01:00:04.001 2.0s",
        "2016-09-15 01:00:07.000 2s"
    ]
    print(solution(lines))

    lines = [
        "2016-09-15 01:00:04.002 2.0s",
        "2016-09-15 01:00:07.000 2s"
    ]
    print(solution(lines))

    lines = [
        "2016-09-15 20:59:57.421 0.351s",
        "2016-09-15 20:59:58.233 1.181s",
        "2016-09-15 20:59:58.299 0.8s",
        "2016-09-15 20:59:58.688 1.041s",
        "2016-09-15 20:59:59.591 1.412s",
        "2016-09-15 21:00:00.464 1.466s",
        "2016-09-15 21:00:00.741 1.581s",
        "2016-09-15 21:00:00.748 2.31s",
        "2016-09-15 21:00:00.966 0.381s",
        "2016-09-15 21:00:02.066 2.62s"
    ]
    print(solution(lines))
