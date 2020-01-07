def solve(a: list) -> int:
    sum = 0
    for i in a:
        sum += i
    return sum

print(solve(list(map(int, input().split()))))