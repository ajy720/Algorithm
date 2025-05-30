table = [25, 10, 5, 1]

if __name__ == "__main__":
    T = int(input())

    for _ in range(T):

        n = int(input())

        for x in table:
            print(n // x, end=" ")
            n %= x

        print()
