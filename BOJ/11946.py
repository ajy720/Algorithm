import sys

input = sys.stdin.readline

if __name__ == "__main__":
  n, m, q = map(int, input().split())

  teams = [[0]*m for _ in ' '*n] 
  ans = [[i+1, 0, 0] for i in range(n)]

  for _ in ' '*q:
    res = input().split()

    time, tNum, pNum = map(int, res[:3])
    tNum -= 1
    pNum -= 1
    res = res[-1]

    if teams[tNum][pNum] == -1:
      continue
    
    if res == "AC":      
      ans[tNum][1] += 1
      ans[tNum][2] += teams[tNum][pNum]*20 + time

      teams[tNum][pNum] = -1
    else:
      teams[tNum][pNum] += 1

  ans.sort(key=lambda x: [-x[1], x[2], x[0]])


  for team in ans:
    print(*team)