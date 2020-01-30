n, k = map(int, input().split())
arr = list(map(int, input().split()))

arr += arr[::-1]

for i in range(len(arr)):
    k -= arr[i]
    if k < 0:
        if i>n-1:
            print(n*2-i)
            exit()
        else:
            print(i+1)
            exit()
    elif k == 0:
        if i>n-1:
            print(n*2-i-1)
        else:
            print(i+2)
            exit()