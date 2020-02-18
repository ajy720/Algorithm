n = int(input())
arr = [0] * (n+1)

for i in range(2, n+1):
    t = []
    if i % 3 == 0:
        t += [arr[i//3]]
    if i % 2 == 0:
        t += [arr[i//2]]
    
    t += [arr[i-1]]

    arr[i] = min(t) + 1

print(arr[n])