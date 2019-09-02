#Mariel Palacios 
#Python-intro-lab1
#Theory of OS
#Fall 2019

import re
import sys
import os
import subprocess

wordList = list()

def readFile():
    # set input and output files
    if len(sys.argv) is not 3:
        print("Correct usage: wordCount.py <input text file> <output file> " )
        exit()

    inputFname = sys.argv[1]
    outputFname = sys.argv[2]

    #create list where words will be saved to


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
            #remove punctuation 
            word = re.sub(r'[^\w\s]', '', line)
            word = re.sub(r'\_', '', word)
            word = re.split('[ \t]', word)

            print(word)

            for currentWord in word:
                wordList.append(currentWord.lower())

            #debug
            print("wordList: ")
            print(wordList)

      
   #write the output to output file
    outputFname = open("output.txt", "w")

    wordList.sort()
    for words in wordList:
        outputFname.write(words + "\n")

    outputFname.close()

    return wordList

    #open and read the file after the appending:
    output = open("output.txt", "r")
    print("\n" + "output: " + "\n")
    print(output.read())



def countWords():
    for words in wordList:
        currentWordCount = wordList.count(words)
        print(words)
        print("word count: ")
        print(currentWordCount)

readFile()
countWords()