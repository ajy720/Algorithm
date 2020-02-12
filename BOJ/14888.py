def cal(num, x, add, sub, mul, div):
    global n, maxv, minv
    if x == n:
        maxv = max(num, maxv)
        minv = min(num, minv)
        return
    else:
        if add :
            cal(num + num_list[x], x+1, add-1, sub, mul, div)
        if sub :
            cal(num - num_list[x], x+1, add, sub-1, mul, div)
        if mul :
            cal(num * num_list[x], x+1, add, sub, mul-1, div)
        if div :
            cal(int(num/num_list[x]), x+1, add, sub, mul, div-1)

maxv = -1000000000
minv = 1000000000

n = int(input())

num_list = list(map(int, input().split()))

a, b, c, d = map(int, input().split())

cal(num_list[0], 1, a, b, c, d)
print(maxv)
print(minv)