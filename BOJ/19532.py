if __name__ == "__main__":
    a, b, c, d, e, f = map(int, input().split())

    aa = a
    bb = b
    cc = c
    dd = d
    ee = e
    ff = f

    x, y = 0, 0

    a *= dd
    b *= dd
    c *= dd
    # print(f"{a}x + {b}y = {c}")

    d *= aa
    e *= aa
    f *= aa
    # print(f"{d}x + {e}y = {f}")

    y = (c - f) // (b - e)
    if aa:
        x = (cc - (bb * y)) // aa
    else:
        x = (ff - (ee * y)) // dd

    print(x, y)
