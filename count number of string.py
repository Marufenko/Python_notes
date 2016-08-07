import re

finalList = []
i = 0
finalSum = 0

hand = open ('regex_sum_304101.txt')
for line in hand:
    line = line.strip()
    x = re.findall('([0-9]+)', line)

    if len(x)>0:
        lineSum = sum(map(int,x))
        finalList.append(lineSum)
        while i < len(finalList):
            finalSum += finalList[i]
            i += 1

print finalSum
