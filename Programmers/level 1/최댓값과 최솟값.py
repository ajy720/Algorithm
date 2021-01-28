def solution(s):
    s = [*map(int, s.split())]

    return f'{min(s)} {max(s)}'

if __name__ == "__main__":
    print(solution(input()))