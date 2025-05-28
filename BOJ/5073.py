if __name__ == "__main__":
    while True:
        [a, b, c] = sorted(map(int, input().split()))

        if a == b == c == 0:
            break

        elif a + b <= c:
            print("Invalid")

        elif a == b == c:
            print("Equilateral")

        elif a != b != c != a:
            print("Scalene")

        else:
            print("Isosceles")
