alphabet = set([chr(x) for x in range(97, 123)])


def solve(string):
    for idx in range(len(string)):
        substring = string[:-idx] if idx else string

        s = set([c for c in substring])
        remain = "".join(sorted(alphabet - s))

        if remain and remain.split(string[-idx])[-1]:
            postfix = remain.split(string[-idx])[-1][0]

            return substring + postfix
    return -1


if __name__ == "__main__":

    print(solve(input()))
