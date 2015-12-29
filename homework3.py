'''You've been handed an encrypted file!
Luckily, you know it's a monoalphabetic
substitution cipher. And thankfully, you
have got a reference corpus of the same
language handy. Finally, you feel so
confident in the sizes of the texts, that
you feel the distributions might just match.

You may assume anything other than the letters
from a-z is unencrypted.'''
import sys
from collections import Counter
def goldbug(encfile="brown-sample-enc.txt", reffile="brown.txt"):
    letters_enc = Counter()
    with open(encfile) as f:
        for line in f:
            for letter in line:
                if letter in 'abcdefghijklmnopqrstuvxyzw':
                    letters_enc[letter] += 1
    letters_ref = Counter()
    with open(reffile) as g:
        for line in g:
            for letterr in line:
                if letterr in 'abcdefghijklmnopqrstuvxyzw':
                    letters_ref[letterr] += 1

    enclist = list(map(lambda x: x[0], letters_enc.most_common()))
    reflist = list(map(lambda x: x[0], letters_ref.most_common()))

    substitutions = {}
    for letter_enc, letter_ref in zip(enclist, reflist):
        substitutions[letter_enc] = letter_ref

    with open(encfile) as f:
        for line in f:
            for letter in line:
                print(substitutions.get(letter,letter), end='')

'''Reads an encrypted file and a reference file and prints
the decrypted text using frequency analysis. Have fun!'''

if __name__ == '__main__':
    goldbug()
