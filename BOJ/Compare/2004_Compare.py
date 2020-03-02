def nCm1(n, m):
    five = getFactorCnt(n, 5) - getFactorCnt(n-m, 5) - getFactorCnt(m, 5)
    two = getFactorCnt(n, 2) - getFactorCnt(n-m, 2) - getFactorCnt(m, 2)

    return min(five, two)

def getFactorCnt(n, t): # n 까지의 자연수를 통틀어 인수 t 의 갯수를 구하는 함수
    tt= t
    ret = 0
    while t <= n:
        ret += n//t
        t *= tt
    
    return ret

def nCm2(n, m):
    if m == 0: c = 1

    if m > n//2: m = n-m

    son = mom = 1

    for i in range(n, n-m, -1): son *= i
    for i in range(1, m+1, 1): mom *= i

    c = son//mom
    ans = 0
    while c % 10 == 0:
        ans += 1
        c//=10
    
    return ans

if __name__ == "__main__":
    for n in range(10000):
        for m in range(n+1):
            ans1 = nCm1(n, m)
            ans2 = nCm2(n, m)
            if ans1 != ans2:
                print(f"오류 발생!!! n: {n}, m: {m}")

