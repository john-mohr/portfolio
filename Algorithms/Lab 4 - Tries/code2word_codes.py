"""
    code2word_codes.py
    Generates 9-letter words from airport codes using a trie of airport codes

    [John David Mohr and Cassidy Orr]
"""

# run "pip3 install pygtrie" or "pip install pygtrie" in the terminal if pygtrie is not found.
import pygtrie as trie  

# read airport codes
codes = []
path_to_code_file = 'airport_codes.txt'
with open(path_to_code_file, 'r') as f:
    codes = f.read().splitlines()

# build a trie using codes
t = trie.CharTrie()
for code in codes:
    t[code] = True

# read nine-letter words
words = []
path_to_word_file = 'nine_letter_words.txt'
with open(path_to_word_file, 'r') as f:
    words = f.read().splitlines()

# extract three potential codes from each nine-letter words,
# and then search for each code in the trie
results = [] # append words, which is a combination of three codes, to results. 
# Your code goes here:

for i in words:
    if t.has_key(i[0:3]):
        if t.has_key(i[3:6]):
            if t.has_key(i[6:9]):
                results.append(i)



## write results into results_codes.txt
with open('results_codes.txt', 'w') as file_handler:
    for word in results:
        file_handler.write("{}\n".format(word)) 