def getFactorCnt(n, t): # n 까지의 자연수를 통틀어 인수 t 의 갯수를 구하는 함수
    ret = 0
    while t <= n:
        ret += n//t
        t **= 2
    
    return ret

if __name__ == "__main__":
    n, t = map(int, input().split())

    cnt = getFactorCnt(n, t)

    print(cnt)