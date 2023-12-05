# Part 1

#from aocd.models import Puzzle 
#data = Puzzle(2023, 2).input_data.split('\n')

filename = 'game_input.txt'

colors = {'red': 12, 
          'green': 13,
          'blue': 14}

valid_game_list = []
with open(filename, 'r') as datafile:
    for line in datafile:
        line_split = line.split(':')
        game_num = int(line_split[0][5:])

        draw_list = [i.split(',') for i in  line_split[1].split(';')]
        draw_valid_list = []
        for draw in draw_list:
            draw_dict = {}
            for i in draw:
                for c in colors.keys():
                    num = int(i.replace(c,'')) if c in i else 0
                    draw_dict[c] = draw_dict.get(c, 0) + num # don't overwrite existing num
            
            # compare draw_dict to colors
            draw_valid = 1 if all(draw_dict[c] <= colors[c] for c in colors) else 0
            draw_valid_list.append(draw_valid)
        
        # check whole game
        game_valid = 1 if all(d == 1 for d in draw_valid_list) else 0
        if game_valid == 1:
            valid_game_list.append(game_num)

print(sum(valid_game_list))

# Part 2

power_list = []
with open(filename, 'r') as datafile:
    for line in datafile:
        line_split = line.split(':')
        draw_list = [i.split(',') for i in  line_split[1].split(';')]

        game_dict = {'red':[], 'green':[], 'blue':[]}
        for draw in draw_list:
            draw_dict={}
            for i in draw:
                for c in colors.keys():
                    num = int(i.replace(c,'')) if c in i else 0
                    draw_dict[c] = draw_dict.get(c, 0) + num # don't overwrite existing num
            for c in colors.keys():
                game_dict[c].append(draw_dict[c])

        for c in colors.keys():
            game_dict[c] = max(game_dict[c])
        
        power = game_dict['red'] * game_dict['green'] * game_dict['blue']
        power_list.append(power)

print(sum(power_list))
