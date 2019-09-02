#Mariel Palacios 
#Python-intro-lab1
#Theory of OS
#Fall 2019

import re
import sys
import os
import subprocess

# set input and output files
if len(sys.argv) is not 3:
    print("Correct usage: wordCount.py <input text file> <output file> " )
    exit()

inputFname = sys.argv[1]
outputFname = sys.argv[2]
#inputFname = sys.argv[3]

wordList = list()

# attempt to open input file
with open(inputFname, 'r') as inputFile:
    for line in inputFile:
        # get rid of newline characters
        line = line.strip()


#line = "   a this is an example of a line. yes no.             ."
        print(len(line))
        print("line: " + line)


        print("stripped: " + line.strip())

        print("split: ")
        wordsInLine = re.split('[ \t]', line)

        print("wordsInLine:")
        print(wordsInLine)

        wordList.append(wordsInLine)
        
        print("wordList: ")
        print(wordList)