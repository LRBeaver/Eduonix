__author__ = 'lyndsay.beaver'
user = input('Enter your name: ')
file_object = open("username.txt", 'a')

file_object.write(user+'\n')
file_object.close()


file_object2=open('username.txt', 'r')
listNames=file_object2.read()
print('The previous list of users of this program were: ')
print(listNames)