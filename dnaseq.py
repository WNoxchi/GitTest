#!/usr/bin/env python2.7

import unittest
from dnaseqlib import *

### Utility classes ###

# Maps integer keys to a set of arbitrary values.
class Multidict:                            # 23-Apr-2017 20:50 - 21:00
    # Initializes a new multi-value dictionary, and adds any key-value
    # 2-tuples in the iterable sequence pairs to the data structure.
    def __init__(self, pairs=[]):
        # raise Exception("Not implemented!")
        self.dict = {}
        # if key unique: add; if not: append
        for pair in pairs:
            if not dict.has_key(pair[0]):
                self.dict[pair[0]] = [pair[1]]
            else:
                self.dict[pair[0]].append(pair[1])
    # Associates the value v with the key k.
    def put(self, k, v):
        # raise Exception("Not implemented!")
        if self.dict.has_key(k):
            self.dict[k].append(v)
        else:
            self.dict[k] = [v]
    # Gets any values that have been associated with the key k; or, if
    # none have been, returns an empty sequence.
    def get(self, k):
        # raise Exception("Not implemented!")
        if self.dict.has_key(k):
            return self.dict[k]
        else:
            return []

# Given a sequence of nucleotides, return all k-length subsequences
# and their hashes.  (What else do you need to know about each
# subsequence?)
def subsequenceHashes(seq, k):              # 23-Apr-2017 19:05 - 20:17
    # raise Exception("Not implemented!")
    subseq = kfasta.subsequences(seq, k)
    RollingHash(subseq)
    while subseq != '':
        yield current_hash(), subseq


# Similar to subsequenceHashes(), but returns one k-length subsequence
# every m nucleotides.  (This will be useful when you try to use two
# whole data files.)
def intervalSubsequenceHashes(seq, k, m):
    raise Exception("Not implemented!")

# Searches for commonalities between sequences a and b by comparing
# subsequences of length k.  The sequences a and b should be iterators
# that return nucleotides.  The table is built by computing one hash
# every m nucleotides (for m >= k).
def getExactSubmatches(a, b, k, m):         # 23-Apr-2017 21:14 - 21:38
    raise Exception("Not implemented!")
    x, y = -k, -k
    while True:
        subseq_a = subsequenceHashes(a, k)
        x += k
        y = -k
        while True:
            subseq_b = subsequenceHashes(b, k)
            y += k
            if subseq_a[0] == subseq_b[0]:
                if subseq_a[1] == subseq_b[1]:
                    yield (x, y)


if __name__ == '__main__':
    if len(sys.argv) != 4:
        print 'Usage: {0} [file_a.fa] [file_b.fa] [output.png]'.format(sys.argv[0])
        sys.exit(1)

    # The arguments are, in order: 1) Your getExactSubmatches
    # function, 2) the filename to which the image should be written,
    # 3) a tuple giving the width and height of the image, 4) the
    # filename of sequence A, 5) the filename of sequence B, 6) k, the
    # subsequence size, and 7) m, the sampling interval for sequence
    # A.
    compareSequences(getExactSubmatches, sys.argv[3], (500,500), sys.argv[1], sys.argv[2], 8, 100)
