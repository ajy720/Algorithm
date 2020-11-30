import sys

input = sys.stdin.readline

if __name__ == "__main__":
    n, q = map(int, input().split())

    arr = [0] + [*map(int, input().split())]

    for _ in ' '*q:
        oper, *o = map(int, input().split())

        if oper == 1:
            a, b = o
            print(sum(arr[a:b+1]))
            arr[a], arr[b] = arr[b], arr[a]

        elif oper == 2:
            a, b, c, d = o
            print(sum(arr[a:b+1]) - sum(arr[c:d+1]))