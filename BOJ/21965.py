if __name__ == "__main__":
    n = int(input())

    arr = [*map(int, input().split())]

    flag = True
    ans = True

    for idx, value in enumerate(arr):
        if not idx:
            continue

        if flag:
            if arr[idx - 1] < arr[idx]:
                continue
            elif arr[idx - 1] == arr[idx]:
                ans = False
                break
            else:
                flag = False

        else:
            if arr[idx - 1] > arr[idx]:
                continue
            else:
                ans = False
                break

    print("YES" if ans else "NO")
