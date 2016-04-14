__author__ = 'lyndsay.beaver'
__author__ = 'lyndsay.beaver'
import re
import random
import urllib
import urllib.request


# http://a4.mzstatic.com/us/r30/Video/v4/2d/1c/6c/2d1c6c1f-9a06-c640-43ca-952355b243e6/poster227x227.jpeg
# <div class="artwork">
# 'src-swap-high-dpi="'
# https://itunes.apple.com/us/movie/ant-man/id1012788984
# https://itunes.apple.com/us/movie/seventh-son/id956943599
# https://itunes.apple.com/us/movie/i-frankenstein/id834760231
# https://itunes.apple.com/us/movie/47-ronin/id773254054
# https://itunes.apple.com/us/movie/enders-game/id723143800
# https://itunes.apple.com/us/movie/avengers-age-of-ultron/id983441161


#url = e.get()

url = input('What is the link: ')
#url = "https://itunes.apple.com/us/movie/ant-man/id1012788984"

x = re.search('movie', url)
y = re.search('/id', url)
start = x.start()+6
end = y.start()
movieName = url[start:end]
# print(movieName)
#ans.configure(text="Movie is: " + str(movieName))
print("Movie is: " + str(movieName))

data = urllib.request.urlopen(url).read()
data1 = data.decode("utf-8")
#print(data1)

m = re.search('/source/', data1)
start = m.start()-100
end = start + 123
newString = data1[start:end]
#print(newString)

l = re.search('/source/', newString)
start= l.end()
end = l.end()+16
imageSize=newString[start:end]
print(imageSize)

k = re.search('/source/', newString)
start=k.end()
end=k.end()+4
startingDigits = newString[start:end]
#print(startingDigits)

if int(startingDigits) >= 600:
    n = re.search('http:', newString)
    start = n.start()
    newString1 = newString[start:]
    print(newString1)
    #print(imageSize)

else:
    print("Use the second part")

fileStart = movieName
fileEnd = ".jpeg"
fileName = fileStart + str(random.randint(1,100)) + fileEnd
print(fileName)

urllib.request.urlretrieve(newString1, fileName)


'''
o = re.search('.jpe', newString1)
#start = 0
end = o.end()
newString2 = newString1[:end]
print(newString2)

p = re.search('poster454x454', newString2)
start = 0
end = p.end() - 13
clippedString = newString2[:end]
print(clippedString)

poster = "poster600x600.jpeg"

newLink = clippedString + poster

print(newLink)

fileStart = "poster600x600"
fileEnd = ".jpeg"
fileName = fileStart + str(random.randint(1,100)) + fileEnd


urllib.request.urlretrieve(newLink, fileName)
'''