default = [1, 1, 2, 2, 2, 8]

if __name__ == "__main__":
    print(*[y - int(x) for x, y in zip(input().split(), default)])
