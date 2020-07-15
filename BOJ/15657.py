def solve(bt, idx):
  if len(bt) == m:
    print(*bt)
    return

  for i, v in enumerate(arr[idx:]):
    solve(bt + [v], i+idx)

if __name__ == "__main__":
    n, m = map(int, input().split())

    arr = sorted(map(int, input().split()))

    solve([], 0)