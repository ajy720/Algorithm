week = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
a, b = map(int, input().split())

print(week[((sum(month[:a-1])+b)%7)])