__author__ = 'lyndsay.beaver'

file_object = open('TestFileName.txt', 'w')
stringVar = 'I can change this text, and have it printed by the other program'

file_object.write(stringVar)
file_object.close()