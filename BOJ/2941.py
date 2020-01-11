croaDict = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
s = input()
for i in croaDict:
    s = s.replace(i, ' ')
print(len(s))