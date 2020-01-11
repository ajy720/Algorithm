s1, s2 = input().split()
print(s1[::-1] if int(s1[::-1]) > int(s2[::-1]) else s2[::-1])