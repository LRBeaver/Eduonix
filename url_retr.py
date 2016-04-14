__author__ = 'lyndsay.beaver'
import urllib

web_data=urllib.urlretrieve('https://docs.python.org/2/library/urllib.html')
print(web_data.read())