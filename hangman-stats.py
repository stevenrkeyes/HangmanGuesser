# Author: Steven Keyes
# Date: 27 July 2013
# Script to see how effectively hangman can be played for English

import csv

import hangman_guesser

# this has the list of words
import CMUcorpus

def numGuessesRequired(word):
    # let's play a game of hangman
    #pattern = "-"*len(word.spelling)
    pattern=''
    numGuesses = 0
    guesses = ""
    
    while pattern != word.spelling and numGuesses<30:
        # make a guess!
        #print "I previously guessed", guesses
        #print "I have made", numGuesses, "wrong guesses."
        guess = hangman_guesser.suggestion(pattern, guesses)[0]
        guesses += guess
        if guess not in word.spelling:
            numGuesses +=1
        #print "I guess the letter",guess

        # if it's in the word, add it to the pattern!
        # first, reset the pattern to the original word
        pattern = word.spelling
        for e in word.spelling:
            if e not in guesses:
                pattern = pattern.replace(e, "-")
        #print pattern

    return numGuesses

if __name__ == "__main__":
    with open("test.csv", 'wb') as f:
        
        # CSV writing object
        w = csv.writer(f)
        
        # dictionary of words and their num guesses req'd
        #r = {}

        l = len(CMUcorpus.words)
        for i in range(l):
            word = CMUcorpus.words[i]
            if i % (l/500) == 0:
                print i, "out of", l
            #print word
            numReqd = numGuessesRequired(word)
            #r[word] = numReqd
            w.writerow([word.spelling, numReqd])

        print "finished guessing words"
        
        #f = r.keys()
        #f.sort(key = lambda x : r[x], reverse=True)
        #for e in f[:50]:
        #    print e, r[e]
    
