def solve():
  n = int(input())
  arr = [0] + [*map(int, input().split())]
  ans = 0

  for i in range(1, n+1):
    p = i

    link = []

    while 1:
      if arr[arr[p]] == 0:
        if arr[p] in link:
          ans += len(link[:link.index(arr[p])])
        else:
          ans += len(link)
        
        break

      link.append(p)     
      cp = p
      arr[cp] = 0
      
      p = arr[p]


  
  return ans
  

if __name__ == "__main__":
    for _ in range(int(input())):
      print(solve())
