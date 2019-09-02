#Mariel Palacios 
#Python-intro-lab1
#Theory of OS
#Fall 2019

import re
import sys
import os
import subprocess

def readFile():
    # set input and output files
    if len(sys.argv) is not 3:
        print("Correct usage: wordCount.py <input text file> <output file> " )
        exit()

    inputFname = sys.argv[1]
    outputFname = sys.argv[2]

    #create list where words will be saved to
    wordList = list()

    # attempt to open input file
    with open(inputFname, 'r') as inputFile:
        for line in inputFile:
            # get rid of newline characters
            #debug
            #print("line: " + line)
            line = line.strip()


            #print(len(line))
            print("current line: " + line)
            # #print("stripped: " + line.strip())

            #split the current line using the whitespace and save  it to temp list wordsInLine
            print("split: ")
            word = re.split('[ \t]', line)
            print(word)

            for currentWord in word:
                wordList.append(currentWord)

            #debug
            print("wordList: ")
            print(wordList)

      



   #write the output to output file
    outputFname = open("output.txt", "w")

    for words in wordList:
        outputFname.write(words)

    outputFname.close()

    #open and read the file after the appending:
    output = open("output.txt", "r")
    print(output.read())


readFile()