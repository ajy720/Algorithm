R = 31
M = 1234567891

if __name__ == "__main__":

    n = int(input())
    s = input()

    res = 0

    for idx, c in enumerate(s):
        res += (ord(c) - 96) * (R**idx) % M

    print(res % M)
