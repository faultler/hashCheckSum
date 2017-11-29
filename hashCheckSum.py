#!/usr/bin/python

import subprocess, os, glob

############################################################
‘’’
this section will define a function to be used later in this main program
the function will take one input:
	directory path
It will then find the only .md5 text file used in that directory using the Python glob library
the function will return a single string that will later be used in a MS comment prompt
‘’’

def createCommandLine(subdirectoryPath):
	textFilePath = glob.glob(subdirectoryPath + ”*.md5”)
	stringToReturn = r”md5deep -r -x “ + textFilePath + r” -e “ + subdirectoryPath
	return stringToReturn

############################################################
‘’’
this section will define a function be used later in this main program
the function will take a string as input
the input string will be run in a MS command terminal and wait for the command to be finished
afterwords, it will return nothing to this main program
‘’’

def runCommand(commandLine):
	process = subprocess,Popen(commandLine)
	process.wait()

############################################################
‘’’
this section will take input from the user regarding directory paths, and text file naming
‘’’

directorInput = input(“Hey buddy! Enter the path to the main directory with the 24 subdirectories: \n”)
print(“\n”)


############################################################
‘’’
create list of all subdirectories
‘’’

createSubdirectories(mainDirectory):
	


############################################################
‘’’
run everything!!!
‘’’
