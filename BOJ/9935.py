def main():
    s = input()
    trigger = input()

    res = []

    for c in s:
        res.append(c)
        if "".join(res[-len(trigger) :]) == trigger:
            for _ in trigger:
                res.pop()

    print("".join(res) if res else "FRULA")


if __name__ == "__main__":
    main()
