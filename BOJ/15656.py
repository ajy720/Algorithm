def solve(bt):
  if len(bt) == m:
    print(*bt)
    return
  
  for i in arr:
    solve(bt + [i])


if __name__ == "__main__":
    n, m = map(int, input().split())

    arr = sorted(map(int, input().split()))

    solve([])