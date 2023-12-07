# Part 1

import numpy as np

filename = 'races.txt'
with open(filename, 'r') as datafile:
    times = datafile.readline().split()[1:]
    distances = datafile.readline().split()[1:]
    races = [(float(times[i]), float(distances[i])) for i in np.arange(len(times))]

def quadratic (t, d):
    x1 = (-t + (t**2 - 4 * d)**.5) / -2
    x2 = (-t - (t**2 - 4 * d)**.5) / -2
    return (x1, x2)

mult = 1
for race in races:
    winning_tuple = quadratic(race[0],race[1])
    double_border = True if winning_tuple[0].is_integer() == True and winning_tuple[1].is_integer() == True else False
    num_wins = winning_tuple[1] - winning_tuple[0] - 1 if double_border else int(winning_tuple[1]) - int(winning_tuple[0]) 
    mult = mult * int(num_wins)

print(mult)


# Part 2 

time = float(''.join(times))
distance = float(''.join(distances))

winning_tuple = quadratic(time,distance)
double_border = True if winning_tuple[0].is_integer() == True and winning_tuple[1].is_integer() == True else False
num_wins = winning_tuple[1] - winning_tuple[0] - 1 if double_border else int(winning_tuple[1]) - int(winning_tuple[0])

print(num_wins)