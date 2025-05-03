from pprint import pprint

SHEEP = "S"
WOLF = "W"
FENCE = "D"
EMPTY = "."

px = [1, 0, -1, 0]
py = [0, -1, 0, 1]


def checkWolfAndInstallFence(arr, x, y):
    for posX, posY in zip(px, py):
        curX, curY = x + posX, y + posY

        if not (0 <= curX < r) or not (0 <= curY < c):
            continue

        if arr[curX][curY] is WOLF:
            return False
        elif arr[curX][curY] is SHEEP or arr[curX][curY] is FENCE:
            continue
        elif arr[curX][curY] is EMPTY:
            arr[curX][curY] = FENCE

    return True


if __name__ == "__main__":
    r, c = map(int, input().split())

    flag = True

    arr = []
    sheeps = []

    for row in range(r):
        s = input()

        for col, value in enumerate(s):
            if value == SHEEP:
                sheeps.append((row, col))

        arr.append([*s])

    for x, y in sheeps:

        flag = checkWolfAndInstallFence(arr, x, y)

        if not flag:
            break

    print(1 if flag else 0)
    if flag:
        print(*["".join(row) for row in arr], sep="\n")
