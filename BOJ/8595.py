alphabet = [chr(x) for x in range(97, 123)] + [chr(x) for x in range(65, 91)]

if __name__ == "__main__":
    n = int(input())
    s = input()

    for x in alphabet:
        s = s.replace(x, " ")

    s = sum(map(int, s.split()))
    print(s)
