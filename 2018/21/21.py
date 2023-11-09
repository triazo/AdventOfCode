#!/usr/bin/python

import sys
import re

alphabet = 'abcdefghijklmnopqrstuvwxyz'

def mod(num, length):
    if num < 0:
        return num + length
    return num % length

def vadd(a, b):
    return (a[0] + b[0], a[1] + b[1])

names = ["addr", "addi", "mulr", "muli",
         "banr", "bani", "borr", "bori",
         "setr", "seti", "gtir", "gtri",
         "gtrr", "eqir", "eqri", "eqrr"]

ops = {
    # add
    "addr": lambda a, b, r: r[a] + r[b],
    "addi": lambda a, b, r: r[a] + b,

    # mul
    "mulr": lambda a, b, r: r[a] * r[b],
    "muli": lambda a, b, r: r[a] * b,

    # AND
    "banr": lambda a, b, r: r[a] & r[b],
    "bani": lambda a, b, r: r[a] & b,

    # OR
    "borr": lambda a, b, r: r[a] | r[b],
    "bori": lambda a, b, r: r[a] | b,

    # set
    "setr": lambda a, b, r: r[a],
    "seti": lambda a, b, r: a,

    # gt
    "gtir": lambda a, b, r: int(a > r[b]),
    "gtri": lambda a, b, r: int(r[a] > b),
    "gtrr": lambda a, b, r: int(r[a] > r[b]),

    # eq
    "eqir": lambda a, b, r: int(a == r[b]),
    "eqri": lambda a, b, r: int(r[a] == b),
    "eqrr": lambda a, b, r: int(r[a] == r[b]),
}

def readprogram(lines):
    program = []

    for line in lines[1:]:
        rx = r'(.+) (.+) (.+) (.+)'
        opcode, a, b, c = re.search(rx, line).groups()
        a = int(a)
        b = int(b)
        c = int(c)

        program.append((opcode, a, b, c))

    return program

def runprogram(registers, program, limit = 10**20):
    r = registers[:]
    ip = 0
    ipr = 1

    clock = 0
    first_state = (1, 7216956)
    states = set()
    last_state = (0, 0)
    while True:
        clock += 1
        if clock % 100000 == 0:
            sys.stdout.write("%d, %d \r" % (clock, len(states)))
            sys.stdout.flush()

        r[ipr] = ip
        if ip < 0 or ip >= len(program):
            print("SUCCESS!")
            print(r)
            break
        i = program[ip]
        #print(ip, i)
        #print(ops[i[0]](i[1], i[2], r))

        if ip == 28:
            if (r[2], r[3]) in states:
                print(last_state)
            states.add(last_state)
            last_state = (r[2], r[3])
        # if ip == 28 or ip == 23 or ip == 9:
        #     print("IP: %d:" % ip)
        # print r
        # print clock, ip

        r[i[3]] = ops[i[0]](i[1], i[2], r)
        ip = r[ipr]
        ip += 1
        if clock > limit:
            return
        #print(r)

    print(registers)
    return


def main():

    sys.setrecursionlimit(2200)

    lines = []
    with open(sys.argv[1], 'r') as f:
        lines = f.read().split('\n')[:-1]



    program = readprogram(lines)

    r = [0, 0, 0, 0, 0, 0]
    i = 0
    #r[0] = 7216956
    runprogram(r, program)
    # while True:
    #     r[0] = i
    #     runprogram(r, program, 1000000)



if __name__ == "__main__":
    main()
