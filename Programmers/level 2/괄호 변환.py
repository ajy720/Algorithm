import sys

sys.setrecursionlimit(10**6)

def checkCorrect(u):
    s = []

    for i in range(len(u)):
        if u[i] == '(':
            s.append('(')
        elif u[i] == ')':
            if s and s[-1] == '(':
                s.pop(-1)
            else:
                return False

    return False if s else True


def solution(p):
    
    # 0. 문자열 p가 빈 문자열이라면 빈 문자열을 반환한다.
    if not p:
        return ""
    
    # 1. 문자열 p를 앞에서부터 '균형잡힌 괄호 문자열'까지 자른다. => u, 남은 문자열 => v
    cnt = {
        "(": 0,
        ")": 0
    }

    for i in range(len(p)):
        cnt[p[i]] += 1

        if cnt["("] == cnt[")"]:
            break

    u = p[:i+1]
    v = p[i+1:]

    # 2-1. 문자열 u가 올바른 괄호 문자열이라면
    if checkCorrect(u):
        # v에 대해서 0단계부터 다시 시작, 결과값을 u에 이어 붙여 반환
        return u + solution(v)
        
    # 2-2. 문자열 u가 올바른 괄호 문자열이 아니라면
    else:    
        #   a. 빈 문자열에 '('를 붙인다.
        #   b. 문자열 v에 대해 0단계부터 다시 시작, 결과값을 a.에 이어 붙임.
        #   c. 마지막에 ')'를 붙임
        ret = '(' + solution(v) + ')'

        #   d. u의 처음과 마지막 문제를 제거하고, 나머지 문자열의 괄호 방향을 반대로 뒤집는다.
        t = ''.join([')' if i == '(' else '(' for i in u[1:-1]])

        #   e. a-b-c. 의 결과값에 d를 이어 붙이고 반환한다.
        return ret + t



if __name__ == "__main__":
    print(solution("(()())()"), "(()())()")

    print(solution(")("), "()")

    print(solution("()))((()"), "()(())()")

