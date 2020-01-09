import sys

n = int(input())


cnt = 0

for i in range(10, n+1):
    temp = []
    flag = 0
    for j in str(i):
        temp.append(int(j))

    d = temp[0] - temp[1]
    for j in range(len(temp)-1):
        if temp[j] - temp[j+1] == d:
            flag = 1
        else :
            flag = 0
    cnt += flag
print(cnt+9)