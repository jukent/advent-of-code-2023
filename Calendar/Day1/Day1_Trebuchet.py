# Part 1

filename = 'calibration_input.txt'

with open(filename, 'r') as datafile:
    data = datafile.read().split()

calibration_values = []
for line in data:
    digits = [int(i) for i in line if i.isdigit()]
    first = digits[0]
    last = digits[-1]
    value = int(str(first)+str(last))
    calibration_values.append(value)

print(sum(calibration_values))


# Part 2

digits_dict = {'one' : 'o1e',
              'two' : 't2o',
              'three' : 't3e',
              'four' : 'f4r',
              'five' : 'f5e',
              'six' : 's6x',
              'seven' :'s7n',
              'eight' : 'e8t',
              'nine' : 'n9e'}

calibration_values_2 = []
for line in data:
    for num in digits_dict.keys():
        line = line.replace(num, digits_dict[num])
    digits = [int(i) for i in line if i.isdigit()]
    first = digits[0]
    last = digits[-1]
    value = int(str(first)+str(last))
    calibration_values_2.append(value)

print(sum(calibration_values_2))