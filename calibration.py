import re

num_words = {'one':1,'two':2,'three':3,
             'four':4,'five':5,'six':6,
             'seven':7,'eight':8,'nine':9}

#p = re.compile(r'\d', re.IGNORECASE)
p = re.compile(r'(?=(\d|'+'|'.join(num_words)+'))', re.IGNORECASE)

calibration_sum = 0

def find_digits(line):
  m = p.findall(line)
  if m[0] in num_words:
    m[0] = num_words[m[0]]
  if m[-1] in num_words:
    m[-1] = num_words[m[-1]]
  return (str(m[0]) + str(m[-1]))

with open('trebuchet_calibration.txt', 'r') as f:
  for line in f:
    calibration_sum += int(find_digits(line))
print(f'The sum of all calibration values is {calibration_sum}.')
