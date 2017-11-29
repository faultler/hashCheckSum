#!/usr/bin/python

import subprocess, os, glob

############################################################
'''
this section will define a function to be used later in this main program
the function will take one input:
	directory path
It will then find the only .md5 text file used in that directory using the Python glob library
the function will return a single string that will later be used in a MS comment prompt
'''
def createCommandLine(subdirectoryPath):
	tempStr = subdirectoryPath + "\*.md5"	#It is assumed that there is only one .md5 file in the subdirectory
	textFilePath = glob.glob(tempStr)[0]	#glob.glob creates list of all .md5 file paths. since there is only one file, I am taking the first element of the list [0]
	stringToReturn = r"md5deep -r -x " + textFilePath + r" -e " + subdirectoryPath		# spaces in quotes are necessary
	return stringToReturn

############################################################
'''
this section will define a function be used later in this main program
the function will take a string as input
the input string will be run in a MS command terminal and wait for the command to be finished
afterwords, it will return nothing to this main program
'''
def runCommand(commandLine):
	process = subprocess,Popen(commandLine)
	process.wait()
############################################################
'''
create list of all subdirectories
example output:

['C:\\Users\\userName\\Desktop\\testing\\FolderA',
 'C:\\Users\\userName\\Desktop\\testing\\FolderB',
 'C:\\Users\\userName\\Desktop\\testing\\FolderC']
'''
def createSubdirectories(mainDirectory):
    listOfSubdirectoryNames = []
    for (dirpath, dirnames, filenames) in os.walk(mainDirectory):
        listOfSubdirectoryNames.extend(dirnames)
        break
    for count in range(len(listOfSubdirectoryNames)):
        tempVar = mainDirectory + "\\"
        listOfSubdirectoryNames[count] = tempVar  + listOfSubdirectoryNames[count]
    return listOfSubdirectoryNames

############################################################
'''
run everything!!!

1. take user input of the mainDirectory
2. run createSubdirectories, which will give a list of all the folders in the mainDirectory
3. create a for statement to iterate through the elements of the list created in stem 2
4. upon each iteration of for statement in step 3; createCommandLine within runCommand.
	as stated in run command's final line, it will wait for the mk5deep to finish before proceeding
'''

#1
tempBool = True
while tempBool = True:
	directoryInput = input("Hey buddy! Enter the path to the main directory with the 24 subdirectories: \n")
	print("\n")
	confirmation = input("Is this correct: \n" + directoryInput + "\n y/n:   ")
	if confirmation = "Y" or "y" or "YES" or "yes" or "Yes" or "yES":
		boolTemp = False
		
#2
subdirectoryList = createSubdirectories(directoryInput)

#3
for element in subdirectoryList:
	#4
	runCommand(createCommandLine(element))
	
	
	
	
	
	
