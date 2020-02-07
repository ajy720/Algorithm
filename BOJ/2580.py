table = []
for _ in range(9):
    table.append(list(map(int, input().split())))

zeros = []
for i in range(9):
     for j in range(9):
         if table[i][j]==0:
             zeros.append((i, j))


def is_promising(i, j):
    promising = [1,2,3,4,5,6,7,8,9]

    for k in range(9):
        if table[i][k] in promising:
            promising.remove(table[i][k])
        if table[k][j] in promising:
            promising.remove(table[k][j])

    i//=3
    j//=3
    for p in range(i*3, (i+1)*3):
        for q in range(j*3, (j+1)*3):
            if table[p][q] in promising:
                promising.remove(table[p][q])

    return promising

flag = False
def dfs(x):
    global flag
    if flag:
        return
    if x == len(zeros):
        for i in table:
            print(*i)
        
        flag = True
        return
    
    else:
        (i, j) = zeros[x]
        promising = is_promising(i, j)

        for num in promising:
            table[i][j] = num
            dfs(x+1)
            table[i][j] = 0

dfs(0)