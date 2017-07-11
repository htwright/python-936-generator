filename = './sample.txt'
import codecs

with open(filename, 'r') as f:
  # f.decode('cp1252')
  content = f.read(15000)
  # print(content)
# print(content)

# print(type(content))


def filter_str(str1, str2):
  for c in str2:
    str1=str1.replace(c,'')
  return str1

# content.translate('.@[]{}()\'\"/\\')
filters = '.@[]{}()\'\"/\\'
content = filter_str(content, filters)
lst = content.split(' ')
# print(lst)


values = {}

for str in lst:
  if str not in values:
    values[str] = 1;
  else:
    values[str] += 1


# print(values)
# with codecs.open(filename, 'a', 'cp1252') as f:
  # print(f)
  # data = f.read(1)
  # print(data)

# sorted(values.iterkeys(), key=lambda k: values[k], reverse = True)

import operator
sorted_values = sorted(values.items(), key=operator.itemgetter(1), reverse=True)

# print(sorted_values)
import random
def generate_936(tuples):
  result = []
  for i in range(4):
    j = random.randint(0, 20)
    x, _ = tuples[j]
    result.append(x)
  # print(result)
  return '%s - %s - %s - %s' % (result[0], result[1], result[2], result[3])
testvar = generate_936(sorted_values)
print(testvar)