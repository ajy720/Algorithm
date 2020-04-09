def lower_bound(k):
    left = 0
    right = len(arr)
     
    while left < right:
        mid = (left+right)//2
     
        if arr[mid] < k: left = mid + 1
        else: right = mid
    
    return right

if __name__ == "__main__":
    arr = []
