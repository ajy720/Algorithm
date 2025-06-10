if __name__ == "__main__":
    arr = [""] * 15
    for _ in " " * 5:
        s = input()

        for idx, c in enumerate(s):
            arr[idx] += c

    print("".join(arr))
