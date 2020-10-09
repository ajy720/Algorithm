def lower_bound(k):
    left = 0
    right = len(arr)

    while left < right:
        mid = (left+right)//2

        if arr[mid][1] < k:
            left = mid + 1
        else:
            right = mid

    return right


if __name__ == "__main__":
    int(input())

    new, k = map(int, input().split())

    arr = [*enumerate(map(int, input().split()))]
    arr.sort(key=lambda x: x[1])

    left = lower_bound(new)
    right = left + 1

    ans = []

    for _ in ' '*k:
      if left < 0:
          ans.append(arr[right][0]+1)
          right += 1
      elif right >= len(arr):
          ans.append(arr[left][0]+1)
          left -= 1
      elif abs(arr[left][1] - new) > abs(arr[right][1] - new):
          ans.append(arr[right][0]+1)
          right += 1
      else:
          ans.append(arr[left][0]+1)
          left -= 1
      
    print(*ans)
