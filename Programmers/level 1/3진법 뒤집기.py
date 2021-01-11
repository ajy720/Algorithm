def solution(n):
    return toBase10(toBase3(n))

def toBase10(arr):
    return sum([(3**i) * arr[i] for i in range(len(arr))])

def toBase3(n):
    arr = []
    while n:
        arr.append(n % 3)
        n //= 3
    
    arr.reverse()
    return arr


if __name__ == "__main__":
    print(solution(45))
    print(solution(125))
