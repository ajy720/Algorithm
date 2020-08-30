import sys

input = sys.stdin.readline


def convert(t): return (t[0]*60+t[1])*100+t[2]


def getTime():
    return convert([*map(int, input().split(':'))])


if __name__ == "__main__":
    time = [getTime() for i in range(3)]

    for _ in range(int(input())):
        record = getTime()
        ans = 0

        for t in time:
            if record > t:
                break
            ans += 1

        print(":(" if ans == 0 else '*'*ans)
