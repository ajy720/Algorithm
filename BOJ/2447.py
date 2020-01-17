
def solve(n : int, x : int , y : int):
    unit = n//3
    for i in range(x+unit, x+unit*2):
        matrix[i][y+unit:y+unit*2]=" " * len(matrix[i][y+unit:y+unit*2])

    if unit == 1:
        return

    for i in range(x, x+(unit*3), unit):
        for j in range(y, y+(unit*3), unit):
            if i == x + unit and j == y + unit:
                continue
            solve(unit, i, j)


n = int(input())

matrix = [['*'] * n for i in range(n)]

solve(n, 0, 0)

for i in range(n):
    print(''.join(matrix[i]))