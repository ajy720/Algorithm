if __name__ == "__main__":
    while True:
        n = input()
        if n == "0":
            break
        l = len(n)
        print("yes" if n[: (l // 2)] == n[(l // 2) + (l % 2) :][::-1] else "no")
