def solution(a, b):
    day = ["FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"]
    month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    return day[(sum(month[:a-1])+b) % 7 - 1]


if __name__ == "__main__":
    a = 1
    b = 1
    print(solution(a, b))
