__author__ = 'lyndsay.beaver'
import re
import random
import urllib
import urllib.request

# https://itunes.apple.com/us/movie/ant-man/id1012788984

# http://a4.mzstatic.com/us/r30/Video/v4/2d/1c/6c/2d1c6c1f-9a06-c640-43ca-952355b243e6/poster227x227.jpeg

#<div class="artwork">

#'src-swap-high-dpi="'
#url = "https://itunes.apple.com/us/movie/seventh-son/id956943599"

url = input('What is the link: ')

data = urllib.request.urlopen(url).read()
data1 = data.decode("utf-8")
#print(data1)

#imageloc = 'src-swap-high-dpi="'
m = re.search('227', data1)
#print(m)

start = m.start()
end = start + 150

newString = data1[start:end]
#print(newString)

n = re.search('dpi="', newString)
start = n.end()
newString1 = newString[start:]
#print(newString1)

o = re.search('.jpeg', newString1)
start = 0
end = o.end()
newString2 = newString1[0:end]
#print(newString2)

p = re.search('poster454x454', newString2)
start = 0
end = p.end() - 13
clippedString = newString2[:end]
#print(clippedString)

poster = "poster600x600.jpeg"

newLink = clippedString + poster

print(newLink)

'''
fileStart = "poster600x600"
for i in range (1,100):
    incremental = i
fileEnd = ".jpeg"
fileName = fileStart + str(incremental) + fileEnd
'''

fileName = fileStart + str(random.randint(1,100)) + fileEnd

#testfile = urllib.URLopener()
#testfile.retrieve(newLink, poster)
urllib.request.urlretrieve(newLink, fileName)