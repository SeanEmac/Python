nums = input().split()
first = nums[0]
second = nums[1]

one = ""
two = ""
for i in range(3):
    one += first[2-i]
    two += second[2-i]

if int(one) > int(two):
    print(one)
else:
    print(two)
