import sys

sys.setrecursionlimit(10**6)

def pow(arr, n):
    if n == 1: return arr

    if n%2 == 0:
        t = pow(arr, n//2)
        return mM(t, t)
    else:
        return mM(pow(arr, n-1), arr)

def mM(arr1, arr2):
    k = len(arr2)
    ret = [[0]*len(arr2[0]) for _ in range(len(arr1))]

    for i in range(len(arr1)):
        for j in range(len(arr2[0])):
            for o in range(k):
                ret[i][j] += (arr1[i][o] * arr2[o][j]) % 1000000

    return ret

if __name__ == "__main__":
    n = int(input())
    powM = pow([[1, 1], [1, 0]], n)

    print(powM[0][1]%1000000)