from readfromsource import readfromfile

data = readfromfile('C:/Users/jeroen.weber/PycharmProjects/aoc2024/day01.txt')
sum = 0
left = []
right = []

def getint(line):
    leftright = line.split()
    return leftright

for line in data:
    leftright = getint(line)
    left.append(leftright[0])
    right.append(leftright[1])

numbers = len(right)

for i in range(len(right)):
    factor = 0
    curleft = left[0]
    for crights in right:
        if (curleft == crights):
            factor += 1
    contribution = factor * eval(curleft)
    sum += contribution
    del(left[0])

print(sum)