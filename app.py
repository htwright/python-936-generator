import codecs
import operator
import random
from collections import Counter
import tkinter as tk
import win32clipboard

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
sorted_values = c.most_common(5000);

def generate_936(tuples = sorted_values):
  result = []
  for i in range(4):
    j = random.randint(0, 4999)
    x, _ = tuples[j]
    result.append(x)
  return '%s - %s - %s - %s' % (result[0], result[1], result[2], result[3])


passwords = []
for i in range(10):
  passwords.append(generate_936(sorted_values))
password = generate_936(sorted_values)


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = password
        self.hi_there["command"] = lambda:self.clipboard(password)
        self.hi_there.pack(side="left")
        for i in passwords[1::2]:
          self.i = tk.Button(self)
          self.i['text'] = i
          self.i['command'] = lambda: self.clipboard(i)
          self.i.pack(side='top')
        for i in passwords[::2]:
          self.i = tk.Button(self)
          self.i['text'] = i
          self.i['command'] = lambda: self.clipboard(i)
          self.i.pack(side='bottom')

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=root.destroy)
        self.quit.pack(side="right")

    def say_hi(self):
        print("hi there, everyone!")
    def reroll(self):
      password = generate_936(sorted_values)
      print(password)
      return password
    def clipboard(self, text):
      copy(text)

def copy(text):
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardText(text, win32clipboard.CF_UNICODETEXT)
    win32clipboard.CloseClipboard()

#single reroll function tied to a single event
#click password to copy passwords
root = tk.Tk()
app = Application(master=root)
app.mainloop()
