if __name__ == "__main__":
    arr = input()
    ans = 0

    for i in arr:
      if i == "S":
        ans += 1
      elif i == "T":
        ans += (4 - ans%4)
      
    print(ans)