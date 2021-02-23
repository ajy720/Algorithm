if __name__ == "__main__":
    n, r, c = map(int, input().split())

    flag = (r + c) % 2

    for i in range(n):
        print(''.join(['v' if (i + j) % 2 == flag else '.'
                        for j in range(n)]))
