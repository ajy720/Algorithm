x = int(input())

temp = 0
i = 0
while x > temp:
    i += 1
    temp += i

x = x - i*(i-1)//2

print(f'{i-x+1}/{x}' if i%2 == 1 else f'{x}/{i-x+1}')