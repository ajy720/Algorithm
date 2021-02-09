def solution(s):
    answer = 0 

    stack = []

    for c in s:
        if stack and stack[-1] == c:
            stack.pop(-1)
        else:
            stack.append(c)

    return 1^bool(stack)

if __name__ == "__main__":
    print(solution(input()))