ans = 0

for _ in ' '*int(input()):
    a, b = map(int, input().split())
    ans += b % a

print(ans)
