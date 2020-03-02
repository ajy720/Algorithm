for _ in range(int(input())):
    n = int(input())
    wear = []
    cnt = []
    for i in range(n):
        
        w, ws = input().split()

        if ws in wear:
            cnt[wear.index(ws)] += 1
        else:
            wear.append(ws)
            cnt.append(2)

    ans = 1
    for i in cnt: ans *= i 

    print(ans-1)