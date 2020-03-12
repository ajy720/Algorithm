import sys

input = sys.stdin.readline

def mM(arr1, arr2):
    k = len(arr2)

    res = [[0]*len(arr2[0]) for _ in range(len(arr1))]

    for i in range(len(arr1)):
        for j in range(len(arr2[0])):
            for o in range(k):
                res[i][j] += arr1[i][o] * arr2[o][j] % 1000

    return res

def pow(arr1, n):
    if n == 1: return arr1

    if n % 2 == 0: 
        t = pow(arr1, n//2)
        return mM(t, t)

    else: return mM(pow(arr1, n-1), arr1)

if __name__ == "__main__":
    n, b = map(int, input().split())

    arr1 = [[*map(int, input().split())] for _ in range(n)]

    for i in pow(arr1, b):
        print(*map(lambda x: x%1000, i))