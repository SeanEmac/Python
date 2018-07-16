left, right = map(int, input().split())
if left + right == 0:
    print("Not a moose")
elif left == right:
    print("Even {}".format(left + right))
else:
    print("Odd {}".format(2 * max(left, right)))