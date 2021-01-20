def solution(s):
    answer = True

    arr = []

    for i in s:
        if i == "(":
            arr.append(i)

        elif i == ")":
            if arr:
                arr.pop(-1)
            else:
                return False

    if arr:
        return False

    return True


if __name__ == "__main__":
    print(solution("()()"), True)
    print(solution("(())()"), True)
    print(solution(")()("), False)
    print(solution("(()("), False)