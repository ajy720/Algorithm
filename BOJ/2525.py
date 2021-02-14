h, m = map(int, input().split())
t = int(input())

t = h*60 + m + t

print((t//60)%24, t%60)