__author__ = 'lyndsay.beaver'

file_object = open('TestFileName.txt', 'r+')
stringVar = 'This is the text that is going into the file' + '\n'
phrase = file_object.read()

newText = file_object.write(stringVar)
newPhrase = file_object.read()

file_object.seek(0,0)

file_object.close()
print("This is the old text: " + phrase + "\n")
print(newPhrase)