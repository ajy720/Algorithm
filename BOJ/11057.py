matrix = [[1]*10]

def solve(i:int):
    matrix[i][0]=1
    for j in range(1, 10):
        matrix[i][j] = (matrix[i-1][j] + matrix[i][j-1]) % 10007

n = int(input())
ans = 0

if n == 1:
    ans =  10

elif n >= 2:    
    for i in range(1, n):
        matrix.append([0]*10)
        solve(i)
    ans = sum(matrix[n-1])

print(ans%10007)