import sys

code = sys.stdin.readlines()

for i in range(len(code)):
    while code[i].find("BUG") != -1:
        code[i] = code[i].replace("BUG", "")

print(*code, sep="")