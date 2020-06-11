import calendar

DAYNAMES = [ "MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY",
             "SATURDAY", "SUNDAY"]

month, day, year = map(int, input().split())
print(DAYNAMES[calendar.weekday(year, month, day)])
