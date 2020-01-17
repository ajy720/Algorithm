ans = 0
for _ in range(int(input())):
    ans += 1 if int(input()) == 1 else -1
print("Junhee is cute!" if ans > 0 else "Junhee is not cute!")