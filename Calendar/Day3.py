import numpy as np
import re
#from aocd.models import Puzzle 

#data = Puzzle(2023, 3).input_data.split('\n')

# Part 1

filename = 'engine_schematic.txt'
with open(filename, 'r') as datafile:
    data = datafile.read().split()

nums_dict = {}
for x in range(len(data)):
    nums_match = list(re.finditer(r'[\d]+', data[x]))
    nums_loc = {(x, m.span()):m.group() for m in nums_match}
    nums_dict.update(nums_loc)

# check if number is next to a symbol
valid_num = []
adj = [[0,1], [1,0], [0,-1], [-1,0], [1,1], [-1,-1], [1,-1], [-1,1]]
for k in nums_dict.keys():

    # find adjacent spaces
    potential_symbol_locs = set()
    columns = np.arange(k[1][0], k[1][1])
    for c in columns:
        potential_symbol_locs.update([(k[0]+a[0], c+a[1]) for a in adj if len(data)>k[0]+a[0]>=0 and len(data[0])>c+a[1]>=0])

    # check for symbol
    valid = False
    for loc in potential_symbol_locs:
        if valid == False:
            if loc is not None:
                value = data[loc[0]][loc[1]]
                if value != '.' and not value.isdigit():
                    valid = True

    if valid == True:
        valid_num.append(int(nums_dict[k]))

print(sum(valid_num))


# Part 2

# check if number is next to a *
gear_dict = {}
for k in nums_dict.keys():
    
    # find adjacent spaces
    potential_symbol_locs = set()
    columns = np.arange(k[1][0], k[1][1])
    for c in columns:
        potential_symbol_locs.update([(k[0]+a[0], c+a[1]) for a in adj if len(data)>k[0]+a[0]>=0 and len(data[0])>c+a[1]>=0])

    # check for *
    for loc in potential_symbol_locs:
        value = data[loc[0]][loc[1]]
        if value == '*':
            if loc not in gear_dict:
                gear_dict[loc] = [int(nums_dict[k])]
            else:
                gear_dict[loc].append(int(nums_dict[k]))

# find ratios
gear_ratios = []
for k in gear_dict.keys():
    if len(gear_dict[k]) == 2:
        ratio = gear_dict[k][0] * gear_dict[k][1]
        gear_ratios.append(ratio)

print(sum(gear_ratios))