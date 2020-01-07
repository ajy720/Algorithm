n = list(map(int, input().split()))

if n == list(range(1, 9)):
    print("ascending")
elif n == list(reversed(range(1, 9))):
    print("descending")
else:
    print("mixed")