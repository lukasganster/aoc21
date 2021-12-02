commands = open("inputs/input2a.txt").read().split("\n")

######## part 1
dict = {}
for i in commands:
    direction, units = i.split(" ")
    if direction in dict.keys(): dict[direction] += int(units)
    else: dict[direction] = int(units)

print(dict["forward"] * (dict["down"] - dict["up"]))

######## part 2
hor, aim, depth = 0, 0, 0
for i in commands:
    direction, units = i.split(" ")
    if(direction == 'forward'):
        hor+=int(units)
        depth+=aim*int(units)
    elif(direction == 'down'): aim += int(units)
    elif(direction == 'up'): aim -= int(units)

print(hor*depth)





