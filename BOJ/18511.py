from itertools import product
from copy import deepcopy


def arrToInt(arr):
    ret = 0
    for idx, val in enumerate(reversed(arr)):
        ret += 10**idx * val

    return ret


def solve(n, k, arr):
    res = 0
    for i in range(len(str(n)), 0, -1):
        if res:
            break

        for case in product(deepcopy(arr), repeat=i):

            case_n = arrToInt(case)
            # print(case_n)
            if n >= case_n:
                res = max(res, case_n)

    return res


if __name__ == "__main__":
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))

    print(solve(n, k, arr))
