__author__ = 'lyndsay.beaver'
import re
import urllib.request

# https://itunes.apple.com/us/movie/ant-man/id1012788984

# http://a4.mzstatic.com/us/r30/Video/v4/2d/1c/6c/2d1c6c1f-9a06-c640-43ca-952355b243e6/poster227x227.jpeg

#<div class="artwork">


url = "https://itunes.apple.com/us/movie/ant-man/id1012788984"

data = urllib.request.urlopen(url).read()
data1 = data.decode("utf-8")
print(data1)

imageloc = 'src-swap-high-dpi="'
m = re.search('src-swap-high-dpi="', data1)
print(m)

start = m.start()
end = start + 150

newString = data1[start:end]
print(newString)

n = re.search('dpi="', newString)
start = n.end()
newString1 = newString[start:]
print(newString1)

o = re.search('" src', newString1)
start = 0
end = o.end()-5
newString2 = newString1[0:end]
print(newString2)

p = re.search('poster280x280', newString2)
start = 0
end = p.end() - 13
clippedString = newString2[:end]
print(clippedString)

poster = "poster600x600.jpeg"

newLink = clippedString + poster

print(newLink)
