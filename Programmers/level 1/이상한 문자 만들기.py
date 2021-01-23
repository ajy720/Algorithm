def subSol(s):
    s = list(s)
    for i in range(0, len(s), 2):
        s[i] = s[i].upper()

    for i in range(1, len(s), 2):
        s[i] = s[i].lower()

    return ''.join(s)

def solution(s):
    return ' '.join([*map(subSol, s.split(' '))])

if __name__ == "__main__":
    print(solution(input()))