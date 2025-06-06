from math import log10

# n자리수 미만의 회문 갯수
bias = [9, 9, 90, 90, 900, 900, 9000, 9000, 90000, 90000]


def calc(n):
    res = sum(bias[: len(n) - 1])

    b = 0

    # n자리수에서는 직접 계산
    half = int(n[: (len(n) + 1) // 2])
    for i in range(10 ** int(log10(half)), half + 1):
        ss = int(str(i) + (str(i)[:-1] if len(n) % 2 else str(i))[::-1])

        if ss <= int(n):
            b += 1

    res += b

    return res


if __name__ == "__main__":
    print(calc(input()))
