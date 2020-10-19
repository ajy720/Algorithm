def calculate(lim):
    t_sum = 0
    for i in range(n):
        if arr[i] <= lim:
            break

        t_sum += arr[i] - lim

    if sum(arr) - t_sum <= m:
        return True
    else:
        return False


def binary_search(left, right):

    while left <= right:
        mid = (left + right) // 2

        if calculate(mid):
            left = mid + 1
        else:
            right = mid - 1

    return right


if __name__ == "__main__":
    n = int(input())

    arr = sorted(map(int, input().split()), reverse=True)

    m = int(input())

    if(sum(arr) <= m):
        print(max(arr))
        exit()

    print(binary_search(0, max(arr)))
