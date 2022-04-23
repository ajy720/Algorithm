import sys

input = sys.stdin.readline

# arr = [0]*10001
d = {}

for i in range(int(input())):
    # arr[int(input())] += 1
    key = input()
    if key in d:
        d[key] += 1
    else:
        d[key] = 1


# for i, a in enumerate(arr):
#     if a == 0: continue
#     print(f"{i}\n"*a, end="")

for num, cnt in sorted(d.items()):
    print(f"{num}\n"*cnt, end="")
    