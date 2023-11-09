#!/usr/bin/python

import sys

alphabet = 'abcdefghijklmnopqrstuvwxyz'

def mod(num, length):
    if num < 0:
        return num + length
    return num % length

def printcircle(circle, i):
    return
    pos = 0
    for j in range(i):
        sys.stdout.write(' ')
        sys.stdout.write(str(pos))
        #sys.stdout.write('%s: %s | ' % (str(pos), str(circle[pos])))
        pos = circle[pos][0]
    print('')



def main():
    lines = []
    with open(sys.argv[1], 'r') as f:
        lines = f.read().split('\n')[:-1]

    players = int(lines[0].split()[0])
    marbles = int(lines[0].split()[6]) * 100
    # marbles = 1618
    # players = 10

    scores = {}
    circle = {0: (0, 0)}
    position = 0
    for i in range(1, marbles):
        if i % 100000 == 0:
            print("marble %d" % i)

        if i % 23 == 0:
            if not i%players in scores:
                scores[i%players] = 0
            scores[i % players] += i

            for n in range(7):
                position = circle[position][1]

            prevpos = circle[position][1]
            nextpos = circle[position][0]
            circle[prevpos] = (nextpos, circle[prevpos][1])
            circle[nextpos] = (circle[nextpos][0], prevpos)



            #print("position is %d" % position)
            #print("removing %d" % position)
            del circle[position]
            scores[i % players] += position


            position = nextpos
            printcircle(circle, i+2)

            continue

        position = circle[position][0]
        nextpos = circle[position][0]
        circle[position] = (i, circle[position][1])
        circle[i] = (nextpos, position)
        circle[nextpos] = (circle[nextpos][0], i)
        position = i

        #circle.insert(position + 1, i)
        #position = (position + 2) % len(circle)
        printcircle(circle, i+2)
        #print(circle)

    print(sorted([scores[p] for p in scores]))



if __name__ == "__main__":
    main()
