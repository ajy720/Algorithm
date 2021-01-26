BASE = [[1, 1], [1, 0]]


def mMultiple(arr1, arr2):
    n = len(arr1)
    m = len(arr2[0])
    k = len(arr2)
    ret = [[0] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            ret[i][j] = sum([arr1[i][t] * arr2[t][j]
                             for t in range(k)]) % 1000000007

    return ret


def mPower(arr, n):
    if n == 1:
        return arr

    tArr = mPower(arr, n//2)

    if n % 2 == 0:
        return mMultiple(tArr, tArr)
    else:
        return mMultiple(mMultiple(tArr, tArr), BASE)


def solve(n):
    return mPower(BASE, n)[0][1] % 1000000007


if __name__ == "__main__":
    print(solve(int(input())))
