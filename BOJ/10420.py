def check(y):
    if (y % 4 == 0 and y % 100 != 0) or y % 400 == 0:
        return True
    else:
        return False


months = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

n = int(input()) - 1

y = 2014
m = 4
d = 2

while 1:
    if months[m] < n + d:
        n -= months[m]
        m += 1

        if m > 12:
            m = m - 12
            y += 1

            if check(y):
                months[2] = 29
            else:
                months[2] = 28

    else:
        d += n
        break

print(f"{y}-{m:02d}-{d:02d}")
