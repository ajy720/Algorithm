a, b = map(int, input().strip().split(' '))

print(*['*' * a] * b, sep='\n')
