from math import gcd, floor, ceil


def solution(w, h):
    answer = 1

    g = gcd(w, h)
    subW, subH = w//g, h//g

    answer = w * h - solve2(subW, subH) * g

    return answer


def solve(w, h):
    x = min(w, h)
    y = max(w, h)

    posY = 0
    ret = 0

    for i in range(1, x+1):
        ret += ceil(y * i / x) - floor(posY)
        posY = y * i / x

    return ret


def solve2(w, h):
    return w + h - 1


if __name__ == "__main__":
    w, h = 8, 12
    print(solution(w, h))
