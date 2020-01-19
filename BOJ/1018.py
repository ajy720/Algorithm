import sys

n, m = map(int, input().split())

arr = sys.stdin.readlines()

for i in range(n):
    arr[i] = list(arr[i].rstrip('\n'))
    for index, j in enumerate(arr[i]):
        arr[i][index] = 1 if j == 'W' else 0

min = 64

for i in range(0, n-7):
    for j in range(0, m -7):
        temp = 0
        for k in range(i, i+8):
            for l in range(j, j+8):
                if k%2^l%2 != arr[k][l]:
                    temp += 1
        
        temp = temp if temp < 64-temp else 64-temp

        if temp < min:
            min = temp

print(min)