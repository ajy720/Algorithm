import sys

input = sys.stdin.readline


def solve():
    n = int(input())
    arr = [0] + [*map(int, input().split())]
    ans = 0

    for i in range(1, n + 1):
        p = i
        link = []
        while 1:
            if arr[p] == 0:
                if p in link:
                    ans += len(link[:link.index(p)])
                    break
                else:
                    ans += len(link)
                    break

            cp = p
            link.append(p)
            p = arr[p]
            arr[cp] = 0

    return ans


if __name__ == "__main__":
    for _ in range(int(input())):
        print(solve())
