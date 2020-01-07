a = []
maxnum = 0
max_i = 0
for i in range(9):
    a.append(int(input()))
    if a[i] > maxnum:
        maxnum = a[i]
        max_i = i

print(maxnum)
print(max_i+1)
