def solution(n:int):
    answer = 0

    cnt = f'{n:b}'.count('1')

    n += 1
    
    while f'{n:b}'.count('1') != cnt:
        n += 1

    return n


if __name__ == "__main__":
    n = int(input())
    print(solution(n))
