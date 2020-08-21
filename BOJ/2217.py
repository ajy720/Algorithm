import sys

input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())

    arr = sorted([int(input()) for _ in ' '*n], reverse=True)
    ans = 0
    for i in range(n):
      ans = max(ans, arr[i]*(i+1))

    print(ans)




