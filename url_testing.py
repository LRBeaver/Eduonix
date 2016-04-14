__author__ = 'lyndsay.beaver'
import urllib.request

web_data=urllib.request.urlopen('https://docs.python.org/2/library/urllib.html')
print(web_data.read())
