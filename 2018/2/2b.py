#!/usr/bin/python2

#!/usr/bin/python

import sys

alphabet = 'abcdefghijklmnopqrstuvwxyz'

def main():
    lines = []
    with open(sys.argv[1], 'r') as f:
        lines = f.read().split('\n')
    lines = [l for l in lines if len(l) > 1]

    for line in lines:
        for line2 in lines:
            difference = 0

            for i in range(len(line)):
                if line[i] != line2[i]:
                    difference += 1
            if difference == 1:
                print (line, line2)



if __name__ == "__main__":
    main()
