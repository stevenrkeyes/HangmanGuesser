# Author: Steven Keyes
# Date: 25 July 2013
# Script to process words in the CMU database to be suitable for hangman

# for reading through the corpus
import csv

# class for words with spellings and frequencies
import word

# location of the CMU database
filename = "CMUCorpusWithCelexFrequenciesGiveToSSVersion.csv"

# identify the columns where frequency and word spelling are listed
wordColumn = list(csv.reader(open(filename)))[0].index("Word")
freqColumn = list(csv.reader(open(filename)))[0].index("CELEX frequency (summed)")

# make words lowercase and contain only the 26 letters
def cleanWord(word):
    return ''.join(e for e in word.lower() if e.islower())
    # or maybe could have used
    #e in string.letters[:26]

# store the words in a list
words = [word.Word(cleanWord(row[wordColumn]),
                   row[min(int(freqColumn),1)]) for row in list(csv.reader(open(filename)))[1:]]
