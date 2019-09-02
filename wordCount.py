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
        # print(word)
        # print("word count: ")
        # print(currentWordCount)
        
    #open and read the file after the appending:
    print(outputFname.read())
    outputFname.close()

readFile()
countWords()