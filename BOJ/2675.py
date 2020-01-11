t = int(input())

for o in range(t):
    r, s = input().split()
    r = int(r)
    for ch in s:
        print(ch*r, end='')

    print()
