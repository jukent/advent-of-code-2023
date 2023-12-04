import numpy as np
import re

# Part 1

filename = 'engine_schematic.txt'

symbols = ['+', '-', '=', '*', '/', '#', '%', '$', '@', '^']
digits = np.arange(0,10)

with open(filename, 'r') as datafile:
    data = datafile.read().split()


symbol_locs = []
num_tuple_list = [] # (num, x, y_0:y_n)
for x in range(len(data)):

    # look for symbols
    symbol_indices = []
    for s in symbols:
        i = [i for i, x in enumerate(data[x]) if x == s]
        symbol_indices.append(i) 

    try:
        symbol_indices = np.hstack(symbol_indices) # flatten
    except:
        pass

    for i in symbol_indices:
        symbol_locs.append((x, int(i))) #f'{x}x{int(i)}')

    # look for numbers
    
    #num_list = [n for n in data[x].split('.') if n.isnumeric()]
    num_list = [n for n in re.split(r'\D+', data[x]) if n.isnumeric()]

    for n in num_list:
        i = data[x].find(n)
        num_tuple_list.append((n, x, np.arange(i, i+len(n)))) # num, row, column

#check if a number is next to a symbol
valid_num = []
for n in num_tuple_list:

    num = n[0]
    row = n[1]
    columns = n[2]

    potential_symbol_locs = []
    # vertical
    for c in columns:
        if row != 0:
            potential_symbol_locs.append((row-1, c)) # north
        if row != 139:
            potential_symbol_locs.append((row+1, c)) # south

    # horizontal
    east = (row, columns[-1]+1) if columns[-1] != 139 else None
    west = (row, columns[0]-1) if columns[0] != 0 else None

    # diagonal
    northeast = (row-1, columns[-1]+1) if row != 0 and columns[-1] != 139 else None
    northwest = (row-1, columns[0]-1) if row != 0 and columns[0] != 0 else None
    southeast = (row+1, columns[-1]+1) if row != 139 and columns[-1] != 139 else None
    southwest = (row+1, columns[0]-1) if row != 139 and columns[0] != 0 else None

    potential_symbol_locs.extend([east, west, northeast, northwest, southeast, southwest])

    if bool(set(potential_symbol_locs).intersection(set(symbol_locs))):
        valid_num.append(int(num))

print(sum(valid_num))