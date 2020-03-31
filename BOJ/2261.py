import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dist(a, b):
    dx = (a[0] - b[0])**2
    dy = (a[1] - b[1])**2
    return dx+dy

def solve(s, e):
    leng = e-s
    if leng == 2:
        return dist(arr[s], arr[s+1])
    if leng == 3:
        return min(dist(arr[s], arr[s+1]), dist(arr[s], arr[s+2]), dist(arr[s+2], arr[s+1]))
    
    leng = (s + e) // 2
    mid = arr[leng][0] # 좌 우 경계선

    d = min(solve(s, leng), solve(leng, e)) # 좌 우 전체에서 거리의 최소값

    arr2 = []
    for i in range(s, e):
        if d >= (mid - arr[i][0])**2: arr2.append(arr[i])
            
    arr2 = sorted(arr2, key=lambda x: x[1])
    if len(arr2) >= 2:
        for i in range(len(arr2)-1):
            for j in range(i+1, len(arr2)):
                if (arr2[i][1] - arr2[j][1])**2 <= d:
                    d = min(d, dist(arr2[i], arr2[j]))
                else: break
    
    return d

if __name__ == "__main__":
    n = int(input())

    arr = sorted([[*map(int, input().split())] for _ in range(n)])

    if len(list(set(map(tuple, arr)))) != n:
        print(0)
    else:
        print(solve(0, n))