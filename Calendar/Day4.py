#from aocd.models import Puzzle 
#data = Puzzle(2023, 4).input_data.split('\n')

# Part 1

filename = 'cards.txt'
with open(filename, 'r') as datafile:
    data = datafile.readlines()

# Part 1

points = 0
for card in data:
    n_winning = card.split('|')[0].split()[2:]
    n_present = card.split('|')[1].split()[0:]

    matches = len(set(n_winning).intersection(set(n_present)))
    c_points = 2**(matches-1) if matches > 0 else 0
    points += c_points
print(points)

# Part 2

winning_dict = {}
for i in np.arange(len(data)):
    n_winning = data[i].split('|')[0].split()[2:]
    n_present = data[i].split('|')[1].split()[0:]

    matches = len(set(n_winning).intersection(set(n_present)))
    winning_dict[i+1] = matches

copies_dict = dict.fromkeys(winning_dict, 1)
for c in winning_dict:
    matches = winning_dict[c]
    copies = copies_dict[c]
    for i in np.arange(c+1, c+matches+1):
        copies_dict[i] += copies

print(sum(copies_dict.values()))
