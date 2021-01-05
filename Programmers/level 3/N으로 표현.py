import sys


def solution(n, number):
    answer = 0
    dp = [0] * (number * n + 1)
    dp[n] = 1

    step = [set() for _ in range(9)]

    for i in range(1, 9):
        step[i].add(int(str(n)*i))

        if int(str(n)*i) < len(dp):
            dp[int(str(n)*i)] = i
            
        for j in range(1, i):

            for o1 in step[j]:
                for o2 in step[i-j]:
                    if o1*o2 == 11:
                        if 1 == 1:
                            pass
                        pass


                    if 0 < o1+o2 < len(dp) and not dp[o1+o2]:
                        step[i].add(o1+o2)
                        dp[o1+o2] = i

                    if 0 < o1-o2 < len(dp) and not dp[o1-o2]:
                        step[i].add(o1-o2)
                        dp[o1-o2] = i

                    if 0 < o2-o1 < len(dp) and not dp[o2-o1]:
                        step[i].add(o2-o1)
                        dp[o2-o1] = i

                    if 0 < o1*o2 < len(dp) and not dp[o1*o2]:
                        step[i].add(o1*o2)
                        dp[o1*o2] = i

                    if 0 < o1//o2 < len(dp) and not dp[o1//o2]:
                        step[i].add(o1//o2)
                        dp[o1//o2] = i

                    if 0 < o2//o1 < len(dp) and not dp[o2//o1]:
                        step[i].add(o2//o1)
                        dp[o2//o1] = i
        
    return dp[number] if dp[number] else -1


if __name__ == "__main__":
    n = 5
    number = 12
    print(solution(n, number))

    n = 2
    number = 11
    print(solution(n, number))

    n = 1
    number = 1121
    print(solution(n, number))
