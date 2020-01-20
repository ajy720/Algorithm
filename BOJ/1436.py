n = int(input())

i = 665
while 1:
    i += 1

    if str(i).count('666') >= 1:
        n -= 1
        if n == 0: break

print(i)