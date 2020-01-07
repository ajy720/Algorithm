n = int(input())

for m in range(n):
    ox = input()

    temp = tot = 0

    for i in ox:
        if i == 'O':
            temp += 1
            tot += temp
        elif i == 'X':
            temp = 0

    print(tot)  