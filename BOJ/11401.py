P = 1000000007

def pow(a, n):
    global P
    if n == 0: return 1

    if n % 2 == 0: return pow(a, n//2)**2 % 1000000007
    else: return a*pow(a, n-1) % 1000000007

def nCk(n, k):
    global P
    if k == 0 or n == k: return 1
    if k > n or k < 0: return 0

    fact = [0, 1, 2]
    for i in range(3, n+1): fact.append((fact[i-1]*i)%P) ##최대 n까지의 팩토리얼이 나오므로 미리 구해놓기

    return (fact[n] * pow((fact[k] * fact[n-k])%P, P-2)) % P

if __name__ == "__main__":
    n, k = map(int, input().split())

    print(nCk(n, k))