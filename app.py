filename = './sample.txt'
import codecs
import operator
import random

with open(filename, 'r') as f:
  content = f.read(15000)


def filter_str(str1, str2):
  for c in str2:
    str1=str1.replace(c,'')
  return str1

filters = '.@[]{}()\'\"/\\'
content = filter_str(content, filters)
lst = content.split(' ')
values = {}

for str in lst:
  if str not in values:
    values[str] = 1;
  else:
    values[str] += 1

sorted_values = sorted(values.items(), key=operator.itemgetter(1), reverse=True)

def generate_936(tuples):
  result = []
  for i in range(4):
    j = random.randint(0, 20)
    x, _ = tuples[j]
    result.append(x)
  return '%s - %s - %s - %s' % (result[0], result[1], result[2], result[3])
testvar = generate_936(sorted_values)
print(testvar)