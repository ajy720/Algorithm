if __name__ == "__main__":

    s = input()

    arr = [s[-x:] for x in [l for l in range(len(s))]]

    print(*sorted(arr), sep="\n")
