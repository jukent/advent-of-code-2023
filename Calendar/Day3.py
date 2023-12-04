import numpy as np
import re

# Part 1

filename = 'engine_schematic.txt'

with open(filename, 'r') as datafile:
    data = datafile.read().split()


num_tuple_list = [] # (num, x, y_0:y_n)
for x in range(len(data)):
    nums_match = list(re.finditer(r'[\d]+', data[x]))
    nums_loc = [(m.group(), x, np.arange(m.start(), m.end())) for m in nums_match]
    num_tuple_list.extend(nums_loc)


# check if number is next to a symbol
valid_num = []
adj = [[0,1], [1,0], [0,-1], [-1,0], [1,1], [-1,-1], [1,-1], [-1,1]]
for n in num_tuple_list:
    
    # find adjacent spaces
    potential_symbol_locs = set()
    for c in n[2]: # columns
        potential_symbol_locs.update([(n[1]+a[0], c+a[1]) for a in adj if len(data)>n[1]+a[0]>=0 and len(data[0])>c+a[1]>=0])

    # check
    valid = False
    for loc in potential_symbol_locs:
        if valid == False:
            if loc is not None:
                value = data[loc[0]][loc[1]]
                if value != '.' and not value.isdigit():
                    valid = True
    
    if valid == True:
        valid_num.append(int(n[0]))

print(sum(valid_num))

# Part 2

gear_candidates = []
for x in range(len(data)):
    indices = [i for i, x in enumerate(data[x]) if x == '*']
    for i in indices:
        gear_candidates.append((x, int(i)))

for c in gear_candidates[0:2]:
    adjacent_indices= [(c[0]+a[0], c[1]+a[1]) for a in adj if len(data)>c[0]+a[0]>=0 and len(data[0])>c[1]+a[1]>=0]

    adjacent_digit_locs = [(i[0],i[1]) for i in adjacent_indices if data[i[0]][i[1]].isdigit()]
    # need to go from digit locations to full numbers