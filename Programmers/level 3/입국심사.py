def check(time: int, n: int, times: list):
    tmp = 0

    for i in times:
        tmp += time // i

        if tmp >= n:
            return True

    return False


def solution(n: int, times: list):
    answer = 0

    times.sort()

    l = 1
    r = times[-1] * n
    while l <= r:
        mid = (l+r)//2

        # print(f'l: {l}, r: {r}, mid: {mid}')

        if check(mid, n, times):
            answer = mid
            r = mid - 1
        else:
            l = mid + 1

    return answer


if __name__ == "__main__":
    print(solution(6, [7, 10]))
    print(solution(7, [1, 2, 3]))
