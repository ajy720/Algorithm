from math import sqrt


def solution(brown, yellow):
    for i in range(1, int(sqrt(yellow))+1):
        if yellow % i == 0:
            x = yellow // i
            y = i

            if brown == 2*x + 2*y + 4:
                return [x+2, y+2]


if __name__ == "__main__":
    print(solution(10, 2), [4, 3])
    print(solution(8, 1), [3, 3])
    print(solution(24, 24), [8, 6])
