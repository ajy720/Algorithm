if __name__ == "__main__":
    n = int(input())

    for i in range(n):
      print(' '*(n-(i+1)) + '*', end='')
      print(' '*(i*2-1), end='')
      if not i == 0: print('*', end='')
      print()