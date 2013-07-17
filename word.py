# Author: Steven Keyes
# Date: 25 July 2013
# class to represent a word

# a word has a spelling and a frequency in its language
class Word(object):
    def __init__(self, spelling, frequency):
        self.spelling = spelling
        self.frequency = int(frequency)

    def __repr__(self):
        return self.spelling
