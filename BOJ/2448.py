def solve(n:int, x:int, y:int):
    unit = n // 2

    for index, i in enumerate(range(x + unit, x + unit*2)):
        matrix[i][y-unit+1+index : y+unit-index] = " " * (unit*2 - index*2 -1) 
        
    if unit == 1:
        return
    solve(unit, x, y)
    solve(unit, x+unit, y+unit)
    solve(unit, x+unit, y-unit)

n = int(input())

matrix = []
for i in range(1, n+1): # 매트릭스 초기화
    temp_str = " "*(n-i)
    temp_str += "*"*(i*2-1)
    temp_str += " "*(n-i)
    
    matrix.append(list(temp_str))

solve(n, 0 , n-1)

for i in matrix:
    print(''.join(i))