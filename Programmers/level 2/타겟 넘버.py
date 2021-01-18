def solution(numbers, target):
    answer = dfs(0, numbers, target)

    return answer

def dfs(n, arr, target):
    if n == target and not arr:
        return 1
    
    if not arr:
        return 0

    ret = 0

    ret += dfs(n + arr[0], arr[1:], target)
    ret += dfs(n - arr[0], arr[1:], target)

    return ret


if __name__ == "__main__":
    print(solution([1,1,1,1,1], 3))
