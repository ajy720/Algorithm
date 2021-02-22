arr = ["baby", "sukhwan", 2, 1,
       "very", "cute", 2, 1,
       "in", "bed", 2, 1,
       "baby", "sukhwan"]

n = int(input())-1

cnt = n // len(arr)
n %= len(arr)

s = arr[n]

if type(s) == int:
    s += cnt
    if s >= 5:
        s = f"tu+ru*{s}"
    else:
        s = "tu" + "ru" * s

print(s)
