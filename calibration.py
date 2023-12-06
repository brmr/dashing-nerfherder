calibration_sum = 0

def find_digit(line):
  return 0

def find_first(line):
  return 0

def find_last(line):
  return 0

with open('trebuchet_calibration.txt', 'r') as f:
  for line in f:
    first_digit = find_first(line)
    second_digit = find_last(line)
    calibration_sum += int(str(first_digit) + str(second_digit))
print(f'The sum of all calibration values is {calibration_sum}.')
