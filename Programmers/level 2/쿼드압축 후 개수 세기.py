def solution(arr):
    answer = [0, 0]

    solve(arr, answer)

    return answer

def solve(arr, answer):
    n = len(arr)

    if check(arr):
        answer[arr[0][0]] += 1
        return 


    arr1 = [subArr[:n//2] for subArr in arr[:n//2]]
    solve(arr1, answer)

    arr2 = [subArr[n//2:] for subArr in arr[:n//2]]
    solve(arr2, answer)

    arr3 = [subArr[:n//2] for subArr in arr[n//2:]]
    solve(arr3, answer)

    arr4 = [subArr[n//2:] for subArr in arr[n//2:]]
    solve(arr4, answer)


def check(arr):
        
    prev = arr[0][0]

    for i in arr:
        for j in i:
            if prev != j:
                return False
            else:
                continue
    
    return True

if __name__ == "__main__":
    arr = [[1, 1, 0, 0],
           [1, 0, 0, 0],
           [1, 0, 0, 1],
           [1, 1, 1, 1]]
    print(solution(arr))

    arr = [[1, 1, 1, 1, 1, 1, 1, 1],
           [0, 1, 1, 1, 1, 1, 1, 1],
           [0, 0, 0, 0, 1, 1, 1, 1],
           [0, 1, 0, 0, 1, 1, 1, 1],
           [0, 0, 0, 0, 0, 0, 1, 1],
           [0, 0, 0, 0, 0, 0, 0, 1],
           [0, 0, 0, 0, 1, 0, 0, 1],
           [0, 0, 0, 0, 1, 1, 1, 1]]
    print(solution(arr))
