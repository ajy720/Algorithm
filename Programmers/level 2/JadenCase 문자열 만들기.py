def solution(s:str):
    return ' '.join(map(lambda x: x.capitalize(), s.split(" ")))


if __name__ == "__main__":
    print(solution(input()))