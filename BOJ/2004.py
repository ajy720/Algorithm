def nCm(n, m):
    five = getFactorCnt(n, 5) - getFactorCnt(n-m, 5) - getFactorCnt(m, 5)
    two = getFactorCnt(n, 2) - getFactorCnt(n-m, 2) - getFactorCnt(m, 2)

    return min(five, two)

def getFactorCnt(n, t): # n 까지의 자연수를 통틀어 인수 t 의 갯수를 구하는 함수
    tt = t
    ret = 0
    while t <= n:
        ret += n//t
        t *= tt
    
    return ret

if __name__ == "__main__":
    n, m = map(int, input().split())

    print(nCm(n, m))