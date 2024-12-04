from readfromsource import readfromfile

data = readfromfile('C:/Users/jeroen.weber/PycharmProjects/aoc2024/day02.txt')
reports = 0
#2 are safe

def getint(line):
    report = line.split()
    return report

def increase(a,b):
    diff = b - a
    if (diff > 0) and (diff <= 3):
        return True
    else:
        return False

for line in data:
    report = getint(line)
    safe = True
    level = 0
    if (eval(report[level+1]) < eval(report[level])):
        report.reverse()
    levels = len(report)-1
    while (safe == True) and (level < levels):
        if (increase(eval(report[level]),eval(report[level+1]))==True):
            level += 1
        else:
            safe = False
    if (safe == True):
        reports += 1

print(reports)