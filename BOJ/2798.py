n, m = map(int, input().split())

c = list(map(int, input().split()))

mAX = 0

for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if c[i]+c[j]+c[k] > mAX and c[i]+c[j]+c[k] <= m:
                mAX = c[i]+c[j]+c[k]
    
print(mAX)