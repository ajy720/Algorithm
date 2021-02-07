from math import gcd

def solution(arr):
    for i in range(1, len(arr)):
        arr[i] = arr[i]*arr[i-1]//gcd(arr[i], arr[i-1])

    return arr[-1]

if __name__ == "__main__":
    arr = [*map(int, input().split())]
    print(solution(arr))