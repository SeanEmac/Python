bought = [int(x) for x in input().split()]
recipe = [int(x) for x in input().split()]

s_ratio = 10000
for x in range(3):
    y = bought[x]/recipe[x]
    if y < s_ratio:
        s_ratio = y

ans = []
for i in range(3):
    ans.append(bought[i] - (recipe[i] * s_ratio))

print("{:.6f} {:.6f} {:.6f}".format(ans[0], ans[1], ans[2]))


