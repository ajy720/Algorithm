import sys

input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())

    result = sorted([float(input()) for _ in range(n)])[:7]

    print(*[f"{score:.3f}" for score in result], sep="\n")
