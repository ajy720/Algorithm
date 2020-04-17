import sys

input = sys.stdin.readline

if __name__ == "__main__":
    n, m = map(int, input().split())

    a = input().split()
    b = input().split()

    for _ in range(int(input())):
        y = int(input())
        print(a[y%n-1]+b[y%m-1])