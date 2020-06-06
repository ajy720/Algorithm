if __name__ == "__main__":
    f = [*map(int, input().split())]
    n = [*map(int, input().split())]

    flag = False

    r = min([f[i]/n[i] for i in range(3)])

    print(*[f[i]-(n[i]*r) for i in range(3)])