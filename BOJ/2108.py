import sys

input = sys.stdin.readline

n = int(input())

arr = []
avg = 0
counting_sort = [0] * 8001

for _ in range(n):
    a = int(input())
    arr.append(a)
    avg += a

    counting_sort[a+4000] += 1

arr.sort()

print(round(avg/n))

# n이 홀수일 때, 짝수일 때 중앙값 구분 필요
if n % 2 == 0: print((arr[n//2]+arr[n//2-1])//2)
else: print(arr[n//2])

# 최빈값 구해야 함
if counting_sort.count(max(counting_sort)) == 1:
    print(counting_sort.index(max(counting_sort))-4000)
else:
    chk = 0
    for i in range(0, 8001):
        if counting_sort[i] == max(counting_sort):
            if chk == 0:
                chk = 1
            else:
                print(i-4000)
                break
        
print(arr[n-1] - arr[0])