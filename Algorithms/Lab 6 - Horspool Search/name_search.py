"""
    name_search.py
    Implementation of string matching algorithms

    [YOUR NAME GOES HERE]
"""

import numpy as np
import argparse

class NameSearch:

    def __init__(self, name_list, name_algorithm, name_length):
        # Matrix with the word search puzzle
        self.matrix = np.load("./data/matrix.npy")
        # Name of the algorithm (BruteForce or Horspool)
        self.algorithm = name_algorithm
        # Length of the name
        self.length = name_length
        # List of all potential names 
        with open("./data/names/" + name_list + ".txt", 'r') as f:
            self.names = f.read().splitlines()
        self.names = [n.upper().strip() for n in self.names]

    def match_brute_force(self, pattern, text):
        # String matching by brute force
        # Your code goes here:
        for i in range(len(text)-len(pattern) + 1):
            j = 0
            while j < len(pattern) and pattern[j] == text[i+j]:
                j += 1
            if j == len(pattern):
                return True
        return False



    def match_horspool(self, pattern, text):
        # String matching by Horspool's algorithm
        # Your code goes here:

        #Creating a the shift table for pattern
        shiftTable = self.shift_table(pattern)

        #shiftIndex holds the right most position of the pattern
        shiftIndex = len(pattern) - 1

        #Loop through all of text until shiftIndex has reached the end
        while shiftIndex < len(text) - 1:
            matchLength = 0

            #If we find a match keep comparing backwards through the pattern
            while matchLength <= len(pattern) - 1 and pattern[len(pattern) - 1 - matchLength] == text[shiftIndex - matchLength]:
                matchLength += 1

            #If matchLength is equal to the length of the pattern we know we have a match
            #If not then shift we need to shift shiftIndex
            if matchLength == len(pattern):
                return True
            else:
                shiftIndex = shiftIndex + shiftTable[ord(text[shiftIndex]) - 65]
        return False


    def shift_table(self,pattern):

        # Creating a table of the default shift value
        table = [None] * 26
        for i in range(len(table)):
            table[i] = len(pattern)

        # Finding the shift values
        for i in reversed(pattern):
            evalChar = []

            #Check to see if we have already evaluated that character
            if i not in evalChar:
                evalChar.append(i)

                #Make sure the last character in pattern is the default shift
                if (len(pattern) - pattern.index(i) - 1 != 0):
                    table[ord(i) - 65] = len(pattern) - self.getIndex(i, pattern) - 1
        return table

    def getIndex(self,character,pattern):
        #Helper method to get the index so we know we have the right most character for the shift
        for i in reversed(range(len(pattern))):
            if(pattern[i] == character):
                if (len(pattern) - i - 1 != 0):
                    return i

    def search(self):
        # pattern is each name in self.names
        # text is each horizontal, vertical, and diagonal strings in self.matrix

        # Your code goes here:

        if self.algorithm == "BruteForce":
            # call self.match_brute_force(pattern, text)
            nRows, nColumns = self.matrix.shape

            #row

            for i in range(nRows):
                row = self.matrix[i, :]
                for pattern in self.names:
                    if self.match_brute_force(pattern, row) and len(pattern) == self.length:
                        print(pattern)
                        return pattern

            #Columns

            for i in range(nColumns):
                column = self.matrix[:,i]
                for pattern in self.names:
                    if self.match_brute_force(pattern, column) and len(pattern) == self.length:
                        print(pattern)
                        return pattern

            #Diagnol
            for i in range(nColumns):
                diagonal = np.diagonal(self.matrix, i)
                for pattern in self.names:
                    if self.match_brute_force(pattern, diagonal) and len(pattern) == self.length:
                        print(pattern)
                        return pattern

            for i in range(nRows)[1:]:
                diagonal = np.diagonal(self.matrix, -i)
                for pattern in self.names:
                    if self.match_brute_force(pattern, diagonal) and len(pattern) == self.length:
                        print(pattern)
                        return pattern





        elif self.algorithm == "Horspool":
            # call self.match_horspool(pattern, text)
            nRows, nColumns = self.matrix.shape

            # row

            for i in range(nRows):
                row = self.matrix[i, :]
                for pattern in self.names:
                    if self.match_horspool(pattern, row) and len(pattern) == self.length:
                        print(pattern)
                        return pattern

            # Columns

            for i in range(nColumns):
                column = self.matrix[:, i]
                for pattern in self.names:
                    if self.match_horspool(pattern, column) and len(pattern) == self.length:
                        print(pattern)
                        return pattern

            # Diagnol
            for i in range(nColumns):
                diagonal = np.diagonal(self.matrix, i)
                for pattern in self.names:
                    if self.match_horspool(pattern, diagonal) and len(pattern) == self.length:
                        print(pattern)
                        return pattern

            for i in range(nRows)[1:]:
                diagonal = np.diagonal(self.matrix, -i)
                for pattern in self.names:
                    if self.match_horspool(pattern, diagonal) and len(pattern) == self.length:
                        print(pattern)
                        return pattern

if __name__ == "__main__":
        
    parser = argparse.ArgumentParser(description='Word Searching')
    parser.add_argument('-name', dest='Name_List', required = True, type = str, help='Name of name list')
    parser.add_argument('-algorithm', dest='Name_Algorithm', required = True, type = str, help='Name of algorithm')
    parser.add_argument('-length', dest='Name_Length', required = True, type = int, help='Length of the name')
    args = parser.parse_args()

    # Example:
    # python name_search.py -algorithm BruteForce -name Hispanic -length 5

    obj = NameSearch(args.Name_List, args.Name_Algorithm, args.Name_Length)
    obj.search()


