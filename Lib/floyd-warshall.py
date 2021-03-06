import sys

INF = sys.maxsize

if __name__ == "__main__":
    n, m = map(int, input().split())

    arr = [[INF] * (n+1) for _ in ' '*(n+1)]

    for i in range(1, n+1):
        arr[i][i] = 0
    
    for _ in ' '*m:
        a, b, weight = map(int, input().split())
        arr[a][b] = weight

    for k in range(1, n+1):
        for a in range(1, n+1):
            for b in range(1, n+1):
                arr[a][b] = min(arr[a][b], arr[a][k] + arr[k][b])

    for i in arr[1:]:
        for j in i[1:]:
            print(j, end="\t")
        print()
