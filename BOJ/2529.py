s = []
ans = []


def solve(bt):
    l = len(bt)
    if l == n+1:
        ans.append(bt)
        return

    elif l == 0:
        for i in range(10):
            solve(bt+str(i))

    else:
        for i in range(10):
            if not str(i) in bt:
                if s[l-1]:
                    if int(bt[-1]) > i:
                        solve(bt+str(i))
                else:
                    if int(bt[-1]) < i:
                        solve(bt+str(i))


if __name__ == "__main__":
    n = int(input())

    s = [True if i == ">" else False for i in input().split()]

    num = [str(i) for i in range(10)]

    solve("")

    ans.sort()
    print(ans[-1])
    print(ans[0])
