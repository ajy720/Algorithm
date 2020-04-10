def binary_search(k):
    left = 0
    right = n-1

    while left <= right:
        mid = (left+right)//2

        if arr[mid] < k: left = mid + 1
        elif arr[mid] > k: right = mid - 1
        else: return True

    return False

if __name__ == "__main__":
    n = int(input())
    arr = sorted([*map(int, input().split())])
    m = int(input())
    chk = [*map(int, input().split())]

    for i in chk:
        print(1 if binary_search(i) else 0, end=" ")