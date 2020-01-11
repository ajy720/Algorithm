ans = 0
for _ in range(int(input())):
    s = input()

    alphaDict = []

    for i, alpha in enumerate(s):
        if alpha not in alphaDict:
            alphaDict.append(alpha)
            continue
        if s[i-1] != alpha:
            ans -= 1
            break
    ans += 1

print(ans)