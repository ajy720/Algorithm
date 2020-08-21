import math

def solve(n):
  prime = get_prime(n)
  ans = 0
  start, end = 0, 1

  while 1:
    s = sum(prime[start:end])

    if s == n:
      ans += 1
      end += 1
    elif s < n:
      end += 1
    elif s > n:
      start += 1
    
    if end > len(prime):
      break
    
  print(ans)

def get_prime(n):
  prime = [True] * (n+1)
  ret = []

  for i in range(2, n+1):
    if prime[i]:
      for j in range(i, n+1, i):
        prime[j] = False
      prime[i] = True    
      ret.append(i)
    else:
      continue

  return ret

if __name__ == "__main__":
    n = int(input())
    solve(n)