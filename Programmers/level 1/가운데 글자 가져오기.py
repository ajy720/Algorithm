def solution(s):
    l = len(s)
    return s[l//2-1+l%2:l//2+1]

if __name__ == "__main__":
    print(solution("abcde"))
    print(solution("qwer"))