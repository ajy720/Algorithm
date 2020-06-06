import sys

document = " ".join([*map(str.strip, sys.stdin.readlines())]).split()

p = ''

for i in document:
    if i == "<br>":
        print(p)
        p = ""

    elif i == "<hr>":
        if p: print(p)
        print("-"*80)
        p = ""

    elif len(p+" "+i) > 80:
        print(p)
        p = i

    else:
        if p: p += " "+i
        else: p = i


print(p)