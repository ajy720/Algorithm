n = int(input())
arr = [*map(int, input().split())]

m = int(input())
t = [*map(int, input().split())]

find = dict()

for i in arr:
    if not i in find:
        find.setdefault(i, 1)
    
    else:
        find[i] += 1

for i in t:
    print(find.get(i) if find.get(i) else 0, end=" ")