#Mariel Palacios 
#Python-intro-lab1
#Theory of OS
#Fall 2019

import re
import sys
import os
import subprocess

#create list where words will be saved to
wordList = list()

def readFile():
    # set input and output files
    if len(sys.argv) is not 3:
        print("Correct usage: wordCount.py <input text file> <output file> " )
        exit()

    inputFname = sys.argv[1]
    outputFname = sys.argv[2]

    # attempt to open input file
    with open(inputFname, 'r') as inputFile:
        for line in inputFile:

            #remove punctuation 
            line = line.replace(".", " ")
            line = line.replace("!", " ")
            line = line.replace("?", " ")
            line = line.replace(";", " ")
            line = line.replace(":", " ")
            line = line.replace(",", " ")
            line = line.replace('"', " ")
            line = line.replace("'", " ")
            line = line.replace("-", " ")       
            #remove whitespace from the line
            line = line.strip()
            #break line into words at the whitespace
            words = re.split('[ \t]', line)            
            
            #add the current word into list of words
            for currentWord in words:
                wordList.append(currentWord.lower())

    return wordList
      

def countWords():
    #write the output to output file
    outputFname = open("output.txt", "w")
    wordList.sort()

    #make a new list to check for repeated words
    newWords = list()

    for word in wordList:
        if word not in newWords:
            if word != "":
                newWords.append(word)
                currentWordCount = wordList.count(word)
                outputFname.write(word + " " + str(currentWordCount) + "\n")

    #open and read the file after the appending:
    #print(outputFname.read())
    outputFname.close()

#call the functions
readFile()
countWords()