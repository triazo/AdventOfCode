#!/usr/bin/python2

#!/usr/bin/python

import sys

alphabet = 'abcdefghijklmnopqrstuvwxyz'

def main():
    lines = []
    with open(sys.argv[1], 'r') as f:
        lines = f.read().split('\n')

    counts = []
    for i in range(26):
        counts.append(0)

    for line in lines:
        newcounts = [c for c in counts]
        for letter in alphabet:
            if line.count(letter) > 1:
                newcounts[line.count(letter)] = counts[line.count(letter)] + 1
        counts = [c for c in newcounts]
        print(counts)


if __name__ == "__main__":
    main()
