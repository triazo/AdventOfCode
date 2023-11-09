#!/usr/bin/python

import sys
import re

offset = 300

alphabet = 'abcdefghijklmnopqrstuvwxyz'

def mod(num, length):
    if num < 0:
        return num + length
    return num % length

def main():
    lines = []
    with open(sys.argv[1], 'r') as f:
        lines = f.read().split('\n')[2:-1]

    initial_state = '#..######..#....#####..###.##..#######.####...####.##..#....#.##.....########.#...#.####........#.#.'
    rules = {}
    for line in lines:
        rules[line[:5]] = line[-1]

    state = '.'*offset + initial_state + '.'*offset
    for t in xrange(200):
        state = '..' + ''.join([rules[state[x-2:x+3]] for x in range(2, len(state) - 2)]) + '..'
        print(state)

    sum = 0
    for i in range(len(state)):
        if state[i] == '#':
            sum += (i - offset)
    print(sum)

    state = '..' + ''.join([rules[state[x-2:x+3]] for x in range(2, len(state) - 2)]) + '..'

    sum = 0
    for i in range(len(state)):
        if state[i] == '#':
            sum += (i - offset)
    print(sum)


if __name__ == "__main__":
    main()
