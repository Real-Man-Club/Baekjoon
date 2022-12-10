import calendar

x, y = map(int, input().split())
week = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]

print(week[calendar.weekday(2007, x, y)])