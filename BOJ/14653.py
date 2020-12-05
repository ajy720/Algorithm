import sys

input = sys.stdin.readline

if __name__ == "__main__":
    n, k, q = map(int, input().split())
    arr = [False] + [True] * (n-1)
    msg = []
    nb_ans = 0
    flag = False

    for i in range(k):
        r, p = input().strip().split()
        r = int(r)
        p = ord(p) - 65
        msg.append([r, p])

        if i == q-1:
            flag = True
            nb_ans = r
    
        if flag:
            arr[p] = False
    
    idx = q-2
    while msg[idx][0] == msg[q-1][0]:
        r, p = msg[idx]
        arr[p] = False

        idx -= 1

    if nb_ans == 0:
        print(-1)
    else:
        print(*[chr(i+65) for i in range(n) if arr[i]])
