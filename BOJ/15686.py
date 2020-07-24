from itertools import combinations
import sys


class Home:

    def __init__(self, x, y):
        self.x = x
        self.y = y


class Chicken:

    def __init__(self, x, y):
        self.x = x
        self.y = y


if __name__ == "__main__":
    n, m = map(int, input().split())
    arr = [[*map(int, input().split())] for _ in ' '*n]

    ans = sys.maxsize
    chickens = []
    homes = []

    for i in range(n):
        for j in range(n):
            if arr[i][j] == 1:
                homes.append(Home(i, j))
            elif arr[i][j] == 2:
                chickens.append(Chicken(i, j))

    for t in combinations(chickens, m):
        cd = 0

        for home in homes:
            cd += min([abs(chicken.x - home.x) + abs(chicken.y - home.y)
                       for chicken in t])

        ans = min(ans, cd)

    print(ans)
