def solution(arr):
    answer = 2
    n = len(arr)

    left = arr[0]
    right = arr[-1]
    for i in range(1, n-1):
        if left > arr[i]:
            left = arr[i]
            answer += 1
        
        if right > arr[-i-1]:
            right = arr[-i-1]
            answer += 1

        if left == right:
            answer -= 1
            break
            
    return answer

if __name__ == "__main__":
    # print(solution([9,-1,-5]))
    print(solution([-16,27,65,-2,58,-92,-71,-68,-61,-33]))