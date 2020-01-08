num = [[0]*10]

def solve(i:int) -> int:
    for j in range(10):
        if j == 0:
            num[i+1][1] += 1*num[i][j]
        elif j == 9:
            num[i+1][8] += 1*num[i][j]
        else:
            num[i+1][j-1] += 1*num[i][j]
            num[i+1][j+1] += 1*num[i][j]
    
n = int(input())
num[0][1:] = [1]*9
for i in range(n-1):
    num.append([0]*10)
    solve(i)

print(sum(num[n-1])%1000000000)