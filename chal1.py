elves = []
file = open("input1.txt", "r")
elve = 0

for line in file:
    if line != '\n':
        elve += int(line)
    else:
        elves.append(elve)
        elve = 0
        
elves.sort()

print(elves[-1 ],elves[-1] + elves[-2] + elves[-3])