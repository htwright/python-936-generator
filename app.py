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
  if len(str) > 3 and str != 'stylebackgroundffffef':
    lst1.append(str.lower())

c = Counter(lst1)
sorted_values = c.most_common(2000);

def generate_936(tuples = sorted_values):
  result = []
  for i in range(4):
    j = random.randint(0, 1999)
    x, _ = tuples[j]
    result.append(x)
  return '%s - %s - %s - %s' % (result[0], result[1], result[2], result[3])


passwords = []
for i in range(10):
  passwords.append(generate_936(sorted_values))
password = generate_936(sorted_values)


class Application(tk.Frame):
    def __init__(self, master = None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.generate_data()

    def clipboard(self, text):
      copy(text)
    def generate_data(self):
      for widget in self.winfo_children():
        widget.destroy()
      self.btn = list(range(10))
      passwords1 = []
      counter = 0
      for i in range(10):
        passwords1.append(generate_936(sorted_values))
      for i in passwords1:
        self.btn[counter] = tk.Button(self, text = i, command = lambda i = i: self.clipboard(i))
        self.btn[counter].pack(side = 'bottom') 
        counter += 1
      self.reroll = tk.Button(self, text = 'reroll', command = self.generate_data)
      self.reroll.pack(side = 'left')
      self.quit = tk.Button(self, text = "QUIT", fg = "red", command = root.destroy)
      self.quit.pack(side = "right")




def copy(text):
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardText(text, win32clipboard.CF_UNICODETEXT)
    win32clipboard.CloseClipboard()

root = tk.Tk()
root.wm_title('936 passwords')
app = Application(master = root)
app.mainloop()
