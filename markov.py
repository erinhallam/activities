# markov.py
#
# Usage:
#   python markov.py 10 "The king" < ShakespeareCorpus.txt
# This will produce at least 10 words of randomized output.
#
# Based on Ben Hoyt's sample code:
# https://benhoyt.com/writings/markov-chain/

import collections, random, sys, textwrap

# Build possibles table indexed by pair of prefix words (word1, word2)
word1 = word2 = ''
possibles = collections.defaultdict(list)
for line in sys.stdin:
    for word in line.split():
        possibles[word1, word2].append(word)
        word1, word2 = word2, word

# Avoid empty possibles lists at end of input
possibles[word1, word2].append('')
possibles[word2, ''].append('')

if len(sys.argv) > 2:
    word1, word2 = sys.argv[2].split(" ")
else:
    word1, word2 = random.choice([k for k in possibles if k[0][:1].isupper()])

# Generate randomized output
output = [word1, word2]
index = 0
minimum = int(sys.argv[1])
while True:
    word = random.choice(possibles[word1, word2])
    output.append(word)
    # Find some punctuation to end with
    if index > minimum and word[-1] in ['.', '?', '!']:
        break
    word1, word2 = word2, word
    index += 1

# Print output wrapped to 70 columns
print(textwrap.fill(' '.join(output)))