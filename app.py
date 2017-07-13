import codecs
import operator
import random
from collections import Counter
filename = './sample.txt'
#current sample.txt file includes 2 text files from wikipedia text dump compiled into a single utf-8.txt in order to avoid errors.
#~6.5 million characters pre filter, ~7MB

#sample1 file includes 13 text files from wikipedia text dump compiled into a single utf-8.txt in order to avoid errors.
#~75 million characters pre filter, ~74MB
with open(filename, 'r', encoding='utf-8') as f:
  content = f.read()
  print('Generating 936 password with %s character sample size. Please wait...' % (len(content)))

def filter_str(str1, str2):
  for c in str2:
    str1=str1.replace(c,'')
  return str1

filters = '.@[]{}()\'\"/\\-=_+;,:!#$%^&*1234567890'
content = filter_str(content, filters)
content = content.replace('\n', ' ').replace('\r', '')

lst = content.split(' ')
values = {}
lst1 = []
for str in lst:
  if len(str) > 3:
    lst1.append(str.lower())

c = Counter(lst1)
# for str in lst1:
#   if str.lower() not in values:
#     values[str.lower()] = 1;
#   else:
#     values[str.lower()] += 1
# #returns sorted (descending) tuples. The program hangs here.
# #TODO: Improve runtime of this step.
# sorted_values = sorted(values.items(), key=operator.itemgetter(1), reverse=True)
sorted_values = c.most_common(5000);
def generate_936(tuples = sorted_values):
  result = []
  for i in range(4):
    j = random.randint(0, 5000)
    x, _ = tuples[j]
    result.append(x)
  return '%s - %s - %s - %s' % (result[0], result[1], result[2], result[3])
passwords = []
for i in range(10):
  passwords.append(generate_936(sorted_values))
print('Length of filtered, sorted list of words')
print(len(sorted_values))
# for i in range(1900,2000):
  # print(sorted_values[i])
password = generate_936(sorted_values)
import tkinter as Tk
import tkinter.tix as Tix

# root = Tix.Tk()
# setup HList
# hl = Tix.HList(root, columns = 5, header = True)
# hl.header_create(0, text = "File")
# hl.header_create(1, text = "Date")
# hl.header_create(1, text = "Size")
# create a multi-column row
# hl.add("row1", text = password)
# hl.item_create(entry_path, 1, text = "2009-03-26 21:07:03")
# hl.item_create(entry_path, 2, text = "200MiB")

import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()
        self.grid()

    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = password
        self.hi_there["command"] = self.reroll()
        self.hi_there.pack(side="top")
        for i in passwords[1::2]:
          self.i = tk.Button(self)
          self.i['text'] = i
          self.i.pack(side='top')
        for i in passwords[::2]:
          self.i = tk.Button(self)
          self.i['text'] = i
          self.i.pack(side='bottom')

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=root.destroy)
        self.quit.pack(side="bottom")

    def say_hi(self):
        print("hi there, everyone!")
    def reroll(self):
      password = generate_936(sorted_values)
      print(password)
      return password

root = tk.Tk()
app = Application(master=root)
app.mainloop()
