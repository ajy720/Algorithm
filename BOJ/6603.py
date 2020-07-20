import sys

sys.setrecursionlimit(10**6)

def solve(bt, n):
  if len(bt) == 6:
    print(*bt)
  
  for i, v in enumerate(arr[n:]):
    solve(bt + [v], i+n+1)

if __name__ == "__main__":
  while 1:
    k, *arr = map(int, input().split())

    if k == 0:
      break

    solve([], 0)
    print()