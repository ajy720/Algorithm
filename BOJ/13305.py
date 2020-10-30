if __name__ == "__main__":
    n = int(input())

    distance = [*map(int, input().split())]
    oil = [*map(int, input().split())]

    ans = 0

    pos = 0
    for i in range(1, n):
        if oil[i] < oil[pos] or i == n-1:
            ans += sum(distance[pos:i]) * oil[pos]
            pos = i

    print(ans)