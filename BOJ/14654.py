win = [0, 0, 0, 2, 1, 3] 
# e.g.) 1(가위) + 2(바위) -> 3(바위)

if __name__ == "__main__":
    n = int(input())

    arrA = [*map(int, input().split())]
    arrB = [*map(int, input().split())]

    winning = True # 연승 state | False가 A팀, True가 B팀
    cnt = 0
    maxCnt = 0

    for a, b in zip(arrA, arrB):
        if a == b:
            maxCnt = max(maxCnt, cnt)

            cnt = 1
            # 비겼다면 연승 카운트를 반대편에게
            winning ^= True

        else:
            if win[a+b] == a and not winning: # A팀이 연승
                cnt += 1

            elif win[a+b] == b and winning: # B팀이 연승
                cnt += 1

            else: # A든 B든 연승이 끊기는 경우
                maxCnt = max(maxCnt, cnt)

                cnt = 1
                # 연승 카운트를 반대편에게
                winning ^= True

    maxCnt = max(maxCnt, cnt)

    print(maxCnt)
