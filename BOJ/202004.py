def lower_bound(k):
    left = 0
    right = len(arr)

    while left < right:
        mid = (left+right)//2

        if arr[mid][1] < k:
            left = mid + 1
        else:
            right = mid

    return right - 1 if right > 0 else right


if __name__ == "__main__":
    n = int(input())
    new, k = map(int, input().split())
    arr = sorted([*enumerate(map(int, input().split()))],
                 key=lambda x: x[1])

    ans = []

    left = lower_bound(new)
    right = left + 1

    for i in range(k):
        if left < 0:
            ans.append(arr[right][0]+1)
            right += 1
            continue
        elif right >= n:
            ans.append(arr[left][0]+1)
            left -= 1
            continue

        if abs(arr[left][1] - new) <= abs(arr[right][1] - new):
            ans.append(arr[left][0]+1)
            left -= 1
        elif abs(arr[left][1] - new) > abs(arr[right][1] - new):
            ans.append(arr[right][0]+1)
            right += 1

    print(*ans)
