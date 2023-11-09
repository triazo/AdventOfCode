#!/usr/bin/python

import sys

def main():
    lines = []
    with open(sys.argv[1], 'r') as f:
        lines = f.read().split('\n')[:-1]

    line = lines[0]

    changed = True
    while changed:
        todelete = {}
        for i in range(len(line)-1):
            if i in todelete:
                continue
            if ord(line[i]) ^ ord(line[i+1]) == 0x20:
                todelete[i] = ''
                todelete[i+1] = ''
        newline = ''.join([line[i] for i in range(len(line)) if not i in todelete])

        if line != newline:
            changed = True
            line = newline
        else:
            changed = False

    print(line)
    print(len(line))



if __name__ == "__main__":
    main()
