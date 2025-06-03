from sys import stdin

input = stdin.readline

if __name__ == "__main__":

    n = int(input())
    tabMedian = [0]
    totalWidth = 0

    for _ in range(n):
        width = int(input())
        totalWidth += width
        tabMedian.append(totalWidth - width / 2)

    screenWidth = int(input())

    for _ in range(int(input())):
        tab = int(input())

        if tabMedian[tab] < screenWidth / 2 or totalWidth < screenWidth:
            res = 0
        elif totalWidth - tabMedian[tab] < screenWidth / 2:
            res = totalWidth - screenWidth
        else:
            res = tabMedian[tab] - screenWidth / 2

        print(f"{res:.2f}")
