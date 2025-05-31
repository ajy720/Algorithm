import heapq
from sys import stdin


input = stdin.readline


def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    ans = 0

    heapq.heapify(arr)

    while len(arr) > 2:
        temp = heapq.heappop(arr) + heapq.heappop(arr)
        ans += temp
        heapq.heappush(arr, temp)

    print(sum(arr) + ans)


if __name__ == "__main__":
    for _ in range(int(input())):
        solve()
