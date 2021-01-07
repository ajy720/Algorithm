import sys


def solution(s):
    answer = sys.maxsize
    n = len(s)

    if n == 1:
        return 1

    for i in range(1, n//2+1):
        compressed = ""
        prev = ""
        cnt = 1

        for j in range(0, n, i):
            subString = s[j:j+i]

            if prev == subString:
                cnt += 1

            else:
                if cnt == 1:
                    compressed += prev
                else:
                    compressed += str(cnt) + prev

                prev = subString
                cnt = 1

        if cnt == 1:
            compressed += prev
        else:
            compressed += str(cnt) + prev

        answer = min(answer, len(compressed))

    return answer


if __name__ == "__main__":
    print(solution("a"))
