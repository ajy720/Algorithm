h,m=map(int,input().split())
s=60
t = h*s+m-45
if t<0:t+=1440
print(t//s,t%s)