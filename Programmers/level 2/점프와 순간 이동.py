def solution(n):
    ans = 0

    while n:
        if n%2 == 1:
            n -= 1
            ans += 1
        else:
            n //= 2

    return ans


if __name__ == "__main__":
    print(solution(int(input())))