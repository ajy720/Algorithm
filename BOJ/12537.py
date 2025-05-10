from functools import reduce


def solve():
    n = int(input())

    reds = []
    blues = []

    for seg in input().split():
        if seg[-1] == "B":
            blues.append(int(seg[:-1]))
        elif seg[-1] == "R":
            reds.append(int(seg[:-1]))

    reds.sort(reverse=True)
    blues.sort(reverse=True)

    loops = zip(reds, blues)

    return reduce(lambda acc, x: acc + x[0] + x[1] - 2, loops, 0) if loops else 0


if __name__ == "__main__":
    for t in range(int(input())):
        print(f"Case #{t+1}: {solve()}")
