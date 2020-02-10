max = -1000000000
min = 1000000000

def dfs(num, op, x, res, nowOp):
    if x == n*2-1:
        global max
        global min
        if max < res: max = res
        if min > res: min = res
        return
    
    if x%2 == 0: # 숫자 삽입
        for i in num:
            tres = 0
            if x == 0: tres = i
            else:
                if nowOp == 0: tres = res + i
                elif nowOp == 1: tres = res - i
                elif nowOp == 2: tres = res * i
                elif nowOp == 3:
                    if res < 0 ^ i < 0:
                        tres = abs(res)//abs(i)
                    else:
                        tres = res // i
            temp = num.copy()
            temp.remove(i)
            dfs(temp, op, x+1, tres, 5)
    
    else : # 연산자 삽입
        for i in range(4):
            if op[i] == 0:
                continue
            else:
                temp = op.copy()
                temp[i] -= 1
                dfs(num, temp, x+1, res, i)


    pass

n = int(input())

num = list(map(int, input().split())) # 숫자

op = list(map(int, input().split())) #연산자

dfs(num.copy(), op.copy(), 0, 0, 0)

print(max)
print(min)

