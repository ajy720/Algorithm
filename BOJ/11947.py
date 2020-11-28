import sys

input = sys.stdin.readline

def inverse(n):
  return int('9'*len(str(n))) - n

def lovely(n):
  return inverse(n) * n

if __name__ == "__main__":

  for _ in ' '*int(input()):
    n = int(input())

    e10 = 10**(len(str(n)))

    if n < e10//2:
      ans = lovely(n)
    else:
      ans = lovely(e10//2)

    print(ans)

