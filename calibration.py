calibration_sum = 0

find_digit(line):

find_first(line):

find_last(line):

with open('calibration_data', 'r') as f:
  for line in f:
    first_digit = find_first(line)
    second_digit = find_last(line)
    calibration_sum += int(str(first_digit) + str(second_digit)
print(f'The sum of all calibration values is {calibration_sum}.')
    
