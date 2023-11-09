#!/usr/bin/python

import sys

def main():
    lines = []
    with open(sys.argv[1], 'r') as f:
        lines = f.read().split('\n')
    lines = [l for l in lines if len(l) > 1]


    fabric = []
    for i in range(1200):
        fabric.append([])
        for j in range(1200):
            fabric[i].append([])

    claims = {}
    for line in lines:
        num = int(line.split(' ')[0].split('#')[1])
        x = int(line.split(' ')[2].split(',')[0])
        y = int(line.split(' ')[2].split(',')[1].split(':')[0])
        w = int(line.split(' ')[3].split('x')[0])
        h = int(line.split(' ')[3].split('x')[1])
        print(num, x, y, w, h)

        claims[num] = ''

        for wi in range(w):
            for hi in range(h):
                fabric[x+wi][y+hi].append(num)


    print(fabric)

    print(claims)

    counter = 0
    for i in range(len(fabric)):
        for j in range(len(fabric[i])):
            if len(fabric[i][j]) >= 2:
                for claim in fabric[i][j]:
                    if claim in claims:
                        del claims[claim]

    print(claims)

    print(counter)
if __name__ == "__main__":
    main()
