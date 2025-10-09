# Jordan Burmylo-Magrann
# File: mode_v1.py
# Program: reads a text file and prints a word with the highest frequency

# Plan:
# Get input file
# Get each word in a list
# Make everything lowercase
# Create dict; key = word, value = freq
# Find highest freq & corresponding word

import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

def main():
    
    # get input file
    fileName = input('Enter a filename: ')
    
    # list of all words in file
    wordList = getWordList(fileName)

    # create dict of words and frequencies
    wordDict = getWordDict(wordList)

    # find word with highest frequency
    maxFreq = findMaxFreq(wordDict)

    # Print word with highest freq
    print(f'The word with the highest frequency is: {maxFreq}')

# Convert all words to lower
# add words to list 

def getWordList(file):
    # open file for reading
    textFile = open(file, 'r')

    # create list of all words
    wordList = textFile.readlines()
    
    # close file
    textFile.close()
    
    for i in range(len(wordList)):
        wordList[i] = wordList[i].lower()
        
    #print(wordList) # Debug
    return wordList


# Create word dictionary from word list with frequencies of each word
def getWordDict(list):
    # create empty word dict
    wordDict = {}

    # key = word, value = freq
    for word in list:
        freq = wordDict.get(word, 0)
        if freq == 0:
            # word entered for first time
            wordDict[word] = 1
        else:
            # word already there
            # update frequency by 1
            wordDict[word] = freq + 1

    #print(wordDict) # debug
    return wordDict


# Find word with highest frequency
def findMaxFreq(dict):
    # find max freq
    maxFreq = max(dict.values())
    #print(maxFreq) # Debug

    for word in dict:
        if dict[word] == maxFreq:
            return word
    return None
    
# execute main program
main()

