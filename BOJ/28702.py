if __name__ == "__main__":
    n = 0
    for i in range(3):
        s = input()
        if s.isdigit():
            n = (3 - i) + int(s)

    if n % 3 and n % 5:
        print(n)
    elif n % 5:
        print("Fizz")
    elif n % 3:
        print("Buzz")
    else:
        print("FizzBuzz")
