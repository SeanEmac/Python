from datetime import date
Day, Month = map(int, input().split())

d = date(2009, Month, Day)

print(d.strftime("%A"))
