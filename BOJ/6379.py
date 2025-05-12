def solve(line: str):
    origin = line.split(", ")

    numbers = []
    words = []

    result = []

    for item in origin:
        if item.isalpha():
            words.append(item)
        else:
            numbers.append(int(item))

    [].sort()
    numbers.sort()
    words.sort(key=str.lower)

    for item in origin:
        if item.isalpha():
            result.append(words.pop(0))
        else:
            result.append(numbers.pop(0))

    return result


if __name__ == "__main__":
    while True:
        line = input()[:-1]

        if line:
            print(*solve(line), sep=", ", end=".\n")
        else:
            break
