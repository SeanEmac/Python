Xvals = []
Yvals = []
for _ in range(3):
    x, y = map(int, input().split())
    Xvals.append(x)
    Yvals.append(y)

new_x = min(Xvals, key=lambda x: Xvals.count(x))
new_y = min(Yvals, key=lambda y: Yvals.count(y))
print(new_x, new_y)