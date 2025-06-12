MAX_T = 0
n, m = 0, 0
arr = []


# O(n)
def process(time):

    res = 0
    for t in arr:
        res += time // t

    return res


# O(log m*max(t))
def binarySearch(start, end):

    if start == end:
        return start

    mid = (start + end) // 2

    if process(mid) >= m:
        end = mid
    else:
        start = mid + 1

    return binarySearch(start, end)


if __name__ == "__main__":

    n, m = map(int, input().split())

    arr = sorted([int(input()) for _ in range(n)])

    MAX_T = m * arr[-1]

    res = binarySearch(0, MAX_T)

    print(res)
