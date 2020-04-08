def search(k):
    left = 0
    right = len(v)-1
     
    while left < right:
        mid = (left+right)//2

        if v[mid] < k: left = mid + 1
        else: right = mid
    
    return right

if __name__ == "__main__":
    n = int(input())
    arr = [*map(int, input().split())]
    v = [arr[0]]

    for i in range(1, n):
        if v[-1] < arr[i]: v.append(arr[i])
        else:
            v[search(arr[i])] = arr[i]

    print(len(v))