def solve(bt):
  if len(bt) == n:
    print(*bt, sep="")
    exit()

  for i in [1, 2, 3]:
    if is_good(bt + [i]):
      solve(bt + [i])


def is_good(arr):
  for i in range(1, len(arr)//2+1):
    if arr[-i:] == arr[-(i*2):-i]:
      return False
  return True

if __name__ == "__main__":
    n = int(input())

    solve([1])