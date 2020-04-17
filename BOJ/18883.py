if __name__ == "__main__":
    n, m = map(int, input().split())

    for i in range(n):
        print(*[m*i+j for j in range(1, m+1)])