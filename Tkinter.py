__author__ = 'lyndsay.beaver'

import tkinter
import re

dir(re)
string = "This is the random string that I will search"
x = re.search("random", string)
print(x)
start = x.start()
end = x.end()
print(string[start:end])