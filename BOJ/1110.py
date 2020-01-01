import sys

input = sys.stdin.readline

n = int(input())
cnt = 0

if(n<10):
    n *= 10

N = n

while 1:    
    cnt+=1
    n = n%10*10 + (n%10 + n//10)%10
    if(N==n):
        break

print(cnt)