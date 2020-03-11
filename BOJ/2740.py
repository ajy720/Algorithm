import sys

input = sys.stdin.readline

if __name__ == "__main__":
    n, k = map(int, input().split())
    arr1 = [[*map(int, input().split())] for i in range(n)]

    k, m = map(int, input().split())
    arr2 = [[] for i in range(m)]
    for i in range(k):
        for index, t in enumerate(input().split()):
            arr2[index].append(int(t))
    
    ans = [([(sum([arr1[i][o] * arr2[j][o] for o in range(k)])) for j in range(m)]) for i in range(n)]     

    for i in ans: print(*i)