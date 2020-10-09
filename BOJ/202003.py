if __name__ == "__main__":
    for _ in ' '*int(input()):
      t1 = [*map(int, input().split())]
      t2 = t1[4:]
      t1[4:] = []

      out = ["R", "S", "I", "R"]
      ans = 0

      if sum(t1) > sum(t2):
        ans += 1
      if max(t1) > max(t2):
        ans += 2
      
      print(out[ans])