a = int(input())
b = int(input())
c = int(input())

n = str(a*b*c)

print(*[n.count(str(i)) for i in range(10)], sep="\n")