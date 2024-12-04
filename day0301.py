from readfromsource import readfromfile
import re

data = readfromfile('C:/Users/jeroen.weber/PycharmProjects/aoc2024/day03.txt')
reports = 0

for line in data:
    matches = re.findall("mul\([0-9]*\,[0-9]*\)",line)
    for multiply in matches:
        matches = re.findall("[0-9]*\,[0-9]*", multiply)
        left = matches[0].split(',')
        evalmul = eval(left[0])*eval(left[1])
        reports += evalmul


print(reports)
