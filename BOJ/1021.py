x=lambda:map(int,input().split());n,m=x();q=list(range(1,n+1));a=0
for f in x():i=q.index(f);a+=min(len(q[i:]),len(q[:i]));q=q[i+1:]+q[:i]
print(a)