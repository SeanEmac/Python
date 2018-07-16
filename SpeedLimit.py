n = int(input())

while n != -1:
    prevT = 0
    total = 0

    for i in range(n):
        speed, time = map(int, input().split())
        total += (speed * (time - prevT))
        prevT = time

    print("{} miles".format(total))
    n = int(input())
