if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input())
        arr = [*map(int, input().split())]

        arr.sort()
        dp = [arr[0] + arr[1]]
        idx = 2
        dpx = 0
        flag = False
        while idx < len(arr) or dpx < len(dp):
            temp = 0
            for _ in range(2):
                if not arr[idx:] and not dp[dpx:]:
                    flag = True
                    break
                elif not arr[idx:]:
                    temp += dp[dpx]
                    dpx += 1
                elif not dp[dpx:]:
                    temp += arr[idx]
                    idx += 1
                elif dp[dpx] >= arr[idx]:
                    temp += arr[idx]
                    idx += 1
                else:
                    temp += dp[dpx]
                    dpx += 1

            if flag:
                break
            dp.append(temp)

        dp2 = dp[dpx:]
        arr = arr[idx:]

        print(sum(dp))
