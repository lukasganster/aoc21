depths = open("inputs/input1b.txt").read().split("\n")
depths = [int(a) for a in depths]

print(depths)
increased = 0

# part 1
for index, value in enumerate(depths):
    behind = depths[index] if index == 0 else depths[index - 1]
    if value > behind:
        increased += 1
# print(increased)

# part 2
increased = 0

for index, value in enumerate(depths[:-3]):
    window_1 = sum(depths[index:index+3])
    window_2 = sum(depths[index+1:index+4])
    if window_1 < window_2:
        increased += 1
# print(increased)

for index, value in enumerate(depths):
    print(index ," - " , value)

