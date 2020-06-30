def solve(bt, n):

    if len(bt) == m:
        print(*bt)

    for i in range(n, len(arr)):
        solve(bt + [arr[i]], i+1)


if __name__ == "__main__":
    n, m = map(int, input().split())
    arr = sorted([*map(int, input().split())])

    solve([], 0)