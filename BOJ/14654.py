win = [0, 0, 0, 2, 1, 3] 
# e.g.) 1(가위) + 2(바위) -> 3(바위)

if __name__ == "__main__":
    n = int(input())

    arrA = [*map(int, input().split())]
    arrB = [*map(int, input().split())]

    winning = True # False가 A팀, True가 B팀
    cnt = [0, 0] # 현재 연승 카운트, cnt[False] = cnt[0], cnt[True] = cnt[1]
    maxCnt = [0, 0] # 최대 연승 카운트, cnt[False] = cnt[0], cnt[True] = cnt[1]

    for a, b in zip(arrA, arrB):
        if a == b:
            # 비겼다면 연승 카운트를 반대편에게
            if winning:
                winning = False
            else:
                winning = True
        else:
            # 이긴 팀에게 연승 카운트를 제공
            if win[a+b] == a:
                winning = False
            elif win[a+b] == b:
                winning = True

        cnt[winning] += 1
