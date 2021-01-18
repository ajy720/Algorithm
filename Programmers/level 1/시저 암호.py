def solution(s, n):
    answer = ''

    s = list(s)

    for i in range(len(s)):
        if s[i] == ' ':
            continue

        if ord('a') <= ord(s[i]) <= ord('z'):
            s[i] = chr((ord(s[i]) + n - ord('a')) % 26 + ord('a'))
        else:
            s[i] = chr((ord(s[i]) + n - ord('A')) % 26 + ord('A'))

    return ''.join(s)


if __name__ == "__main__":
    # print(solution('AB', 1))
    print(solution('z', 1))
    print(solution('a B z', 4))
