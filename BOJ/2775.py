matrix = [[0]*15 for _ in range(15)]

def solve(k:int, n:int) -> int:
    if matrix[k][n]!=0:
        return matrix[k][n]

    if k == 0:
        matrix[k][n] = n
        return n
    elif n == 1:
        matrix[k][n] = 1
        return 1
    

    matrix[k][n] = solve(k-1, n)+solve(k, n-1)
    return matrix[k][n]

for _ in range(int(input())):
    k = int(input())
    n = int(input())
    print(solve(k, n))