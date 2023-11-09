#!/usr/bin/python

import sys

def main():
    lines = []
    with open(sys.argv[1], 'r') as f:
        lines = f.read().split('\n')

    freqs = {}
    x = 0
    n = 0
    while True:
        n += 1
        print(n, len(freqs))
        for l in lines:
            if len(l) < 1:
                continue
            sign = l[0]=='+'
            num = int(l[1:])
            freqs[x] = ''
            x += (-1, 1)[sign] * num
            if x in freqs:
                print("DUPLICATE")
                print(x)
                sys.exit(1)

    print x

if __name__ == "__main__":
    main()
