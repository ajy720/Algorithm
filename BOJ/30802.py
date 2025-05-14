if __name__ == "__main__":
    n = int(input())

    arr = [x for x in list(map(int, input().split())) if x]

    t, p = map(int, input().split())
    print(sum([x // t + (1 if x % t else 0) for x in arr]))
    print(n // p, n % p)
