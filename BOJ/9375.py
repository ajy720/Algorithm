for _ in range(int(input())):
    n = int(input())
    cnt = {}
    for i in range(n):
        
        w, ws = input().split()

        if ws in cnt:
            cnt[ws] += 1
        else:
            cnt.setdefault(ws, 2)

    ans = 1
    for i in cnt.keys(): ans *= cnt[i] 

    print(ans-1)