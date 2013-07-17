# Author: Steven Keyes
# Date: 25 July 2013
# Script to guess words for hangman

# for searching for words using regex
import re
import string

# this has the list of words
import CMUcorpus

# words is a list of word objects
def filterNletters(words, n):
    return [word for word in words if len(word.spelling)==n]

# words is a list of word objects; letters can be a string or a list of letters
def withoutLetters(words, letters):
    return [word for word in words if all(l not in word.spelling for l in letters)]

# pattern like "-u--i-g" for running with u, i, and g guessed
def withPattern(words, pattern):
    pattern = string.replace(pattern, "-",".")
    
    # return words of the correct length
    # and that have the patterned letters in the correct place
    # and that have no more instances of patterned letters (like "riders" shouldn't match ----r-)
    return [word for word in filterNletters(words,len(pattern)) \
            if bool(re.match(pattern, word.spelling)) \
            and all(word.spelling.count(e)==pattern.count(e) for e in pattern.replace(".",""))] 

# function to suggest words for hangman
# pattern like "-u--i-g" for running with u, i, and g guessed
# guesses like "kmaf"
def suggestWords(pattern, guesses):
    # start ith all possible words
    possibleWords = CMUcorpus.words
    
    # i'm assuming guesses just contains wrong guesses
    # but just in case, we'll remove the correct guesses
    guesses = [e for e in guesses if e not in pattern]

    # remove words that don't fit the pattern
    possibleWords = withPattern(possibleWords, pattern)
    
    # remove words that have eliminated letters
    possibleWords = withoutLetters(possibleWords, guesses)

    return possibleWords


# suggest letters by the number of words that have them
def suggestLettersWordCount(pattern, guesses):
    possibleWords = suggestWords(pattern, guesses)

    letterFreq = {}

    possibleLetters = [e for e in string.letters.lower()[:26] if e not in pattern and e not in guesses]
    for l in possibleLetters:
        letterFreq[l] = sum(1 for w in possibleWords if l in w.spelling)

    return letterFreq

# suggest letters by the number of words that have them, weighted by the frequency of the word
def suggestLettersFreq(pattern, guesses):
    possibleWords = suggestWords(pattern, guesses)

    letterFreq = {}

    possibleLetters = [e for e in string.letters.lower()[:26] if e not in pattern and e not in guesses]
    for l in possibleLetters:
        letterFreq[l] = sum(w.frequency for w in possibleWords if l in w.spelling)

    return letterFreq

def suggestion(pattern, guesses, freq=True):
    if freq:
        # list of letters keying their frequencies
        d = suggestLettersFreq(pattern, guesses)
    else:
        d = suggestLettersWordCount(pattern, guesses)
    # list of letters
    f = d.keys()
    #print "The most common letters for this pattern and their counts are the following."
    f.sort(key = lambda x : d[x], reverse=True)
    #for e in f:
    #    print e, d[e]
    return f
        
