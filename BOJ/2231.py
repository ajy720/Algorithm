n = int(input())
if n < 20:    
    for i in range(0, n):
        sum = i
        for j in str(i):
            sum += int(j)
        if sum == n:
            print(i)
            exit()
            #break
    print(0)
    exit()    

for i in range(n - len(str(n))*9, n):
    sum = i
    for j in str(i):
        sum += int(j)
    if sum == n:
        print(i)
        exit()
        #break
print(0)