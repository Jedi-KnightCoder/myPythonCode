#Task 1
#Complete the function to return the current working directory
import os
def getCurrentDirectory():
    return os.getcwd()
print(getCurrentDirectory())

#print(help(os))

#Task 2 Complete the function to return the directory name only from the given file name
def getDirectoryName(fileName):
    #return dir(fileName)
    #return os.path.dirname(fileName)
    return os.path.realpath(fileName)
print(getDirectoryName("/var/www/test.html"))
print(getDirectoryName("/var/www/apple/test.html"))

#print(help(os.path))
# Task 3
# Complete the function to return the file name part only from the given file name
def getFileName(fileName):
       return os.path.basename(fileName)
print(getFileName('main.py'))



#Task 4 Complete the function to return the directory name only from the given file name
def createFile(filename):
    c = open(filename, 'w')
    c.write('howdy')
    c.close()
    return filename
print(createFile('test.txt'))

#Task 5 Complete the function to print all files in the given directory
def printFiles(someDirectory):
    #print(someDirectory)
    #print(someDirectory)
    print(os.listdir(someDirectory))
printFiles(os.getcwd())

#Task 6 #Complete the function to return FILE if the given path is
# a file or return DIRECTORY if the given #path is a directory or
# return NEITHER is it's not a file or directory
#print(os.listdir(os.getcwd())[0])
def whatIsIt(somePath):
    if os.path.isdir(somePath):
        return 'DIRECTORY'
    elif os.path.isfile(somePath):
        return 'FILE'
    else:
        return 'NEITHER'
print(whatIsIt(os.getcwd()))  # expected output: DIRECTORY
print(whatIsIt(os.listdir(os.getcwd())[2]))  # expected output: FILE
print(whatIsIt('apple.pie.123.txt'))

#Task 7 Complete the function to read the contents of the specified file and print the contents
def printFileContents(filename):
    f = open(filename, 'r')
    d = f.read()
    print(d)
    f.close()
printFileContents("test.txt")

#Task 8
#Complete the function to append the given new data
#to the specified file then print the contents of the file
def appendAndPrint(filename, newData):
    f = open(filename, 'a+')
    #with open(filename, 'w+') as f:
    f.write(" Hello" + " " + newData)
    f = open(filename, 'r')
    print(f.read())
    f.close()
print(appendAndPrint("test.txt", "World"))
# expected output: Hello World




