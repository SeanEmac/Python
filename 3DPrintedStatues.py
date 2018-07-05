from math import log, ceil

n = int(input())

days = ceil(log(n, 2) + 1)
print(days)
