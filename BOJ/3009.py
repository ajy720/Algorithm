x = [0]*3
y = [0]*3
for i in range(3):
    x[i], y[i] = map(int, input().split())

for i in range(3):
    if x.count(x[i]) == 1:
        x = x[i]
        break

for i in range(3):
    if y.count(y[i]) == 1:
        y = y[i]
        break

print(x, y)