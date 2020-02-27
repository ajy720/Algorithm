s = input().split("-")

print(sum(list(map(int , s[0].split("+")))) - sum([sum(list(map(int, sub.split("+")))) for sub in s[1:]]))