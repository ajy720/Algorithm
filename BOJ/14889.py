import sys

minv = sys.maxsize

def dfs(x, team1):
    global minv
    if x == n//2+1: #여기서 dfs 종료. team1과 team2 분리
        sum1 = 0
        sum2 = 0
        team2 = list(set([i for i in range(1, n+1)]) - set(team1))
        for i in range(n//2):
            for j in range(i, n//2):
                sum1 += arr[team1[i]-1][team1[j]-1] + arr[team1[j]-1][team1[i]-1]
                sum2 += arr[team2[i]-1][team2[j]-1] + arr[team2[j]-1][team2[i]-1]
        
        minv = min(minv, abs(sum1-sum2))
        return

    for i in range(team1[-1] if team1 else 1, n+1):
        if i not in team1: dfs(x+1, team1+[i])
        if x == 1: break

n = int(input())
arr = []

for i in range(n):
    arr.append(list(map(int, input().split())))

dfs(1, [])

print(minv)