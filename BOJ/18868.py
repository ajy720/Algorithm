if __name__ == "__main__":
    n, m = map(int, input().split())
    arr = [[*map(int, input().split())] for _ in range(n)]
    cnt, flag = 0, False

    for i in range(n-1):
        for j in range(i+1, n):
            flag = False
            for k in range(m-1):
                for o in range(k+1, m):
                    a = arr[i][k] - arr[i][o]
                    b = arr[j][k] - arr[j][o]
                    if a == 0 and b == 0:
                        continue
                    elif a * b > 0:
                        continue
                    else:
                        flag = True
                        break
                if flag: break
            if flag: continue
            else: cnt += 1

    print(cnt)