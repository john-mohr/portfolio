"""
    Hangman.py
    Plays a game of hangman

    [John David Mohr]
"""

import sys
import random


class Hangman:
    """
    A class for playing a game of hangman
    """

    def __init__(self):
        """
        Initializes the words list
        """
        file = open('words.txt', 'r')
        self.words = []
        self.wordguess = []
        for line in file:
            self.words.append(line.rstrip())


    def printword(self):
        """
        Outputs the current status of the guesses
        """
        for c in self.wordguess:
            print(c, end="")
        print()

    def playgame(self):
        """
        Plays a game of hangman allowing for a maximum of 10 guesses
        """
        # generate random word
        word = 'dwindled' #self.words[random.randint(0, len(self.words) - 1)]
        # print word
        self.wordguess = ['_'] * len(word)

        guesses = 0
        guessedChar = []

        while guesses < 10:
            print("Guesses:", end="")
            print(guesses)
            ch = input('Enter a guess:').lower()

            #List of false values representing values that need to be guessed
            wordMap = [False] * len(word)

            ### Your code goes here:###
            #Checking that the input meets the correct conditions
            if ch.isalpha() & (len(ch)==1) & (ch not in guessedChar):
                guessedChar.append(ch)
                guesses += 1

                #Check if the character is in the word
                if ch in word:
                    #If the guess matches a charachter in the word we set its position to true
                    for i in range(len(word)):
                        if(word[i] == ch):
                            wordMap[i] = True
                    #Create a list of chars using word map as a guide to determine where characters go
                    wordList = list(map(lambda guess: ch if guess == True else '_', wordMap))

                    #Changing wordguess characters to the guessed character
                    for i in range(len(word)):
                        if self.wordguess[i] != wordList[i]:
                            if self.wordguess[i] == '_':
                                self.wordguess[i] = wordList[i]

                #Win condition, statement and return
                if '_' not in self.wordguess:
                    self.printword()
                    print("Good Job. You Win")
                    return






            else:
                print("Guess must be alphabetic, a single letter, and not the same guess twice")

            self.printword()
        print("Sorry you ran out of guesses.")

if __name__ == "__main__":
    game = Hangman()

    game.playgame()
