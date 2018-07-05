import math

line = input().split()

n = int(line[0])
width = int(line[1])
height = int(line[2])

diagonal = math.sqrt(width*width + height*height)

for i in range(n):
    if int(input()) <= diagonal:
        print('DA')
    else:
        print('NE')

