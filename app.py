import codecs
import operator
import random
filename = './sample1.txt'
#current sample file includes 6 text files from wikipedia text dump compiled into a single utf-8.txt in order to avoid errors.
#~31 million characters pre filter, ~31MB
with open(filename, 'r', encoding='utf-8') as f:
  content = f.read()


def filter_str(str1, str2):
  for c in str2:
    str1=str1.replace(c,'')
  return str1
print(len(content))
filters = '.@[]{}()\'\"/\\-=_+;,:!#$%^&*'
content = content.lower()
content = filter_str(content, filters)
print(len(content))
lst = content.split(' ')
values = {}
lst1 = []
for str in lst:
  if len(str) > 6:
    lst1.append(str)

for str in lst1:
  if str not in values:
    values[str] = 1;
  else:
    values[str] += 1
#returns sorted (descending) tuples
sorted_values = sorted(values.items(), key=operator.itemgetter(1), reverse=True)

def generate_936(tuples):
  result = []
  for i in range(4):
    j = random.randint(0, 500)
    x, _ = tuples[j]
    result.append(x)
  return '%s - %s - %s - %s' % (result[0], result[1], result[2], result[3])
testvar = generate_936(sorted_values)
print(testvar)
print(len(sorted_values))