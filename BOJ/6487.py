def _solve(p1, p2):
    # ax + by + c = 0
    # cy = ax + b

    try:
        a = (p1[1] - p2[1]) / (p1[0] - p2[0])
        b = p1[1] - (a * p1[0])
        c = 1

    except ZeroDivisionError as e:
        a = 1
        b = -p1[0]
        c = 0

    return a, b, c


def solve(p1, p2, p3, p4):
    a, b, c = _solve(p1, p2)
    d, e, f = _solve(p3, p4)

    # print(f"{c}y = {a}x + {b}")
    # print(f"{f}y = {d}x + {e}")

    if a == d:
        if b == e:
            print("LINE")
        else:
            print("NONE")
    else:
        x, y = 0, 0
        if not c:
            x = -b / a
        elif not f:
            x = -e / d

        if not a:
            y = b / c
        elif not d:
            y = e / f

        if not x:
            x = -(b - e) / (a - d)

        if not y:
            y = a * x + b

        print(f"POINT {x:.2f} {y:.2f}")


if __name__ == "__main__":
    n = int(input())

    for _ in range(n):
        x1, y1, x2, y2, x3, y3, x4, y4 = map(int, input().split())
        solve((x1, y1), (x2, y2), (x3, y3), (x4, y4))
        # print()
