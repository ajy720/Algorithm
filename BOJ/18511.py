n, k = input().split()
s = sorted(list(map(int, input().split())), reverse = True) + [0]

ans = [int(i) for i in n]
flag = False
'''
for i in reversed(range(len(n))):
    if flag:
        if ans[i]-1 > min(s):
            ans[i]-=1
            while ans[i] not in s:
                ans[i] -= 1
            flag = False
        elif i == 0:
            ans = [max(s) for i in range(len(n)-1)]
            print(ans)
            exit() 
        else: continue
    
    if min(s) > ans[i]:
        ans[i] = max(s)
        flag = True
        continue
    
    while ans[i] not in s:
        ans[i] -= 1

'''
'''
for i in range(len(ans)):
    if flag:
        ans[i] = max(s)

    if ans[i] in s:
        flag = False
        continue
    
    else:
        while ans[i] not in s:
            ans[i] -= 1

            if ans[i] < 0:
                c = 1
                while ans[i-c]-1 not in s:
                    if i-c < 0:
                        ans = [max(s) for i in range(len(n)-1)]
                        print(ans)
                        exit()

                    ans[i-c] -= 1
                    if ans[i-c] < 0:
                        c += 1
                        continue

        flag = True

'''





print(ans)
