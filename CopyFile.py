__author__ = 'lyndsay.beaver'
orig_file = input("What is the name of your file? : " )

orig_file = orig_file + ".txt"
file1 = open(orig_file, "r")
file2 = open("copiedfile.txt", "w")
file2.write(file1.read())
file1.close()
file2.close()