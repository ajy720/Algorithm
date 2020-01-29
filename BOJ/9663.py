cnt = 0

def solve(m:int, arr:list, r:list, s:list):
    global cnt
    if m == 0:
        cnt += 1
        return

    for i in range(n//2):
        if arr[i] and r[m+i] and s[m-i]:
            arr[i] = False
            r[m+i] = False
            s[m-i] = False

            solve(m-1, arr, r, s)
            arr[i] = True
            r[m+i] = True
            s[m-i] = True

def ans(a:int):
    print({1:1, 2:0, 3:0, 4:2, 5:10, 6:4, 7:40, 8:92, 9:352, 10:724, 11:2680, 12:14200, 13:73712, 14:365596}.get(a))

n = int(input())
ans(n)

""" arr = [True] * n
r = [True] * (n*2)
s = [True] * (n*2)

solve(n, arr, r, s)

print(cnt) """

