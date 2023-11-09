#!/usr/bin/python

import sys

alphabet = 'abcdefghijklmnopqrstuvwxyz'

def mod(num, length):
    if num < 0:
        return num + length
    return num % length

def main():
    lines = []
    with open(sys.argv[1], 'r') as f:
        lines = f.read().split('\n')[:-1]

    players = int(lines[0].split()[0])
    marbles = int(lines[0].split()[6]) * 100
    # marbles = 1618
    # players = 10

    scores = {}
    circle = [0]
    position = 0
    for i in range(1, marbles):
        if i % 100000 == 0:
            print("marble %d" % i)

        if i % 23 == 0:
            if not i%players in scores:
                scores[i%players] = 0
            scores[i % players] += i
            scores[i % players] += circle[mod(position - 8, len(circle))]

            # print("position is %d" % position)
            # print("removing %d from position %d" % (circle[position - 8], mod(position - 8, len(circle))))
            position = mod(position - 8, len(circle))
            del circle[position]
            position = (position + 1) % len(circle)
            #del circle[mod(position - 8, len(circle))]

            #print(circle)
            continue

        circle.insert(position + 1, i)
        position = (position + 2) % len(circle)
        #print(circle)

    print(sorted([scores[p] for p in scores]))



if __name__ == "__main__":
    main()
