from readfromsource import readfromfile
import re

data = readfromfile('C:/Users/jeroen.weber/PycharmProjects/aoc2024/day03.txt')
reports = 0
#2 are safe

def increase(a,b):
    diff = b - a
    if (diff > 0) and (diff <= 3):
        return True
    else:
        return False

def isSafeReport(report):
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
    return safe

for line in data:
    matches = re.findall("mul\([0-9]*\,[0-9]*\)",line)
    for multiply in matches:
        matches = re.findall("[0-9]*\,[0-9]*", multiply)
        left = matches[0].split(',')
        evalmul = eval(left[0])*eval(left[1])
        reports += evalmul


print(reports)
