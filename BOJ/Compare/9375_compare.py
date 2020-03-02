for _ in range(int(input())):
    n = int(input())
    cnt = {}
    
    wear = []
    cnt2 = []

    log = []
    for i in range(n):
        log.append(list(input().split()))

        if log[i][1] in cnt:
            cnt[log[i][1]] += 1
        else:
            cnt.setdefault(log[i][1], 2)

        if log[i][1] in wear:
            cnt2[wear.index(log[i][1])] += 1
        else:
            wear.append(log[i][1])
            cnt2.append(2)

    ans = 1
    for i in cnt.keys(): ans *= cnt[i] 

    ans2 = 1
    for i in cnt2: ans2 *= i 

    if ans != ans2:
        print(f"오류 발생!!\nlog:\n{log}\ncnt:\n{cnt}\ncnt2:\n{cnt2}")