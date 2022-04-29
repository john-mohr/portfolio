"""
    code2word_words.py
    Generates 9-letter words from airport codes using a trie of 9-letter words

    [John David Mohr, Cassidy Orr]
"""
# run "pip3 install pygtrie" or "pip install pygtrie" in the terminal if pygtrie is not found.
import pygtrie as trie

# read nine-letter words
words = []
path_to_word_file = 'nine_letter_words.txt'
with open(path_to_word_file, 'r') as f:
    words = f.read().splitlines()

# build a trie using nine-letter words
t = trie.CharTrie()
for word in words:
    t[word] = True

# read airport codes
codes = []
path_to_code_file = 'airport_codes.txt'
with open(path_to_code_file, 'r') as f:
    codes = f.read().splitlines()

# generate all possible nine letter words from the airport codes
# and then search for each word in the trie
results = [] # append words, which is a combination of three codes, to results. 
# Your code goes here:

for i in codes:
    if t.has_subtrie(i):
        for x in codes:
            if t.has_subtrie(i+x):
                for y in codes:
                    if t.has_key(i+x+y):
                        results.append(i+x+y)






## write results into results_words.txt
with open('results_words.txt', 'w') as file_handler:
    for word in results:
        file_handler.write("{}\n".format(word)) 