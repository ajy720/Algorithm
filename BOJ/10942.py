import sys

input = sys.stdin.readline

def is_palindrom(s, e):
    global arr

    while s <= e:
        if arr[s] != arr[e]:
            return False
        s +=1
        e -=1

    return True


if __name__ == "__main__":
    global arr

    n = int(input().strip())
    arr = [*map(int, input().split())]
    ans = []

    for _ in range(int(input())):
        s, e = map(int, input().split())

        if (s+e) in ans:
            print(1)
        elif is_palindrom(s-1, e-1):
            ans.append(s+e)
            print(1)
        else:
            print(0)