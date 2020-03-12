import sys

input = sys.stdin.readline

def mM(arr1, arr2):
    k = len(arr2)

    res = [[0]*len(arr2[0]) for _ in range(len(arr1))]


    for i in range(len(arr1)):
        for j in range(len(arr2[0])):
            for o in range(k):
                res[i][j] += arr1[i][o] * arr2[o][j]

    return res
                
if __name__ == "__main__":
    n, k = map(int, input().split())
    arr1 = [[*map(int, input().split())] for i in range(n)]

    k, m = map(int, input().split())
    arr2 = [[*map(int, input().split())] for i in range(k)]
    
    for i in mM(arr1, arr2):
        print(*i)