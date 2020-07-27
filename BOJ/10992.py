if __name__ == "__main__":
    n = int(input())

    for i in range(1, n):
      print(' '*(n-i), end="")
      s = [' ']*(i*2-1)
      s[0] = s[-1] = '*'
      print(''.join(s))

    print('*'*(n*2-1))