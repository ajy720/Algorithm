from math import sqrt

l, h, w = map(int, input().split())

l **= 2
h **= 2
w **= 2

h2 = int(sqrt(l * h/(h+w)))
w2 = int(sqrt(l * w/(w+h)))

print(h2, w2)
