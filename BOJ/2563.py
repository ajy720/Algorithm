arr = [[0]*101 for i in range(101)]

for _ in range(int(input())):
    a, b = map(int, input().split())
    
    for i in range(b, b+10):
        arr[i][a:a+10] = [1]*10
    
ans = [sum(i) for i in arr]
print(sum(ans))