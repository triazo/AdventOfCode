#!/usr/bin/python

import sys
import re

alphabet = 'abcdefghijklmnopqrstuvwxyz'

def mod(num, length):
    if num < 0:
        return num + length
    return num % length

def printboard(board, elves, goblins):
    for y, line in enumerate(board):
        row = []
        units = []
        for x, c in enumerate(line):
            if (y, x) in elves:
                row.append('E')
                units.append("E(%d), "%elves[(y,x)][0])
            elif (y, x) in goblins:
                row.append('G')
                units.append("G(%d), "%goblins[(y,x)][0])
            else:
                row.append(c)
        print(''.join(row) + '   ' + ''.join(units))

def printdistances(board, elves, goblins, distances):
    for y, line in enumerate(board):
        row = []
        for x, c in enumerate(line):
            if (y, x) in distances:
                row.append(str(distances[(y,x)]))
            elif (y, x) in elves:
                row.append('E')
            elif (y, x) in goblins:
                row.append('G')
            else:
                row.append(c)
        print(''.join(row))

def merge(x, y):
    z = x.copy()
    z.update(y)
    return z

def move(board, elves, goblins, unit):
    enimes = (elves, goblins)[unit in elves]
    units = merge(elves, goblins)
    adjtiles = set([])
    for e in enimes:
        adjtiles = adjtiles.union({c for c in adj(e)})

    inrange = {t for t in adjtiles if not (board[t[0]][t[1]] == '#' or t in units)}

    # choose where to go
    distances = {unit: 0}
    curd = 0
    while True:
        tostarts = {d for d in distances if distances[d] == curd}
        curd += 1
        if len(tostarts) == 0:
            break
        toadds = set([])
        for s in tostarts:
            toadds = toadds.union(set(adj(s)))
        realadds = {p for p in toadds if not (p in distances or p in units or board[p[0]][p[1]] == '#')}
        for p in realadds:
            distances[p] = curd

    # choose the best target
    mind = 999999
    for p in inrange:
        if not p in distances:
            continue
        if distances[p] < mind:
            mind = distances[p]

    targets = {p for p in inrange if p in distances and distances[p] == mind}
    # can there be no targets? Only if none of the 'inrange' are reachable
    if len(targets) == 0:
        return unit

    target = sorted(targets)[0]
    #print("target: %s"%(str(target)))

    # calculate distance to target for whole board
    distances = {target: 0}
    curd = 0
    while True:
        tostarts = {d for d in distances if distances[d] == curd}
        curd += 1
        if len(tostarts) == 0:
            break
        toadds = set([])
        for s in tostarts:
            toadds = toadds.union(set(adj(s)))
        realadds = {p for p in toadds if not (p in distances or p in units or board[p[0]][p[1]] == '#')}
        for p in realadds:
            distances[p] = curd

    #printdistances(board, elves, goblins, distances)
    # Now choose which of the four adj(unit) to go to
    mind = 999999
    options = [p for p in adj(unit) if not (p in units or board[p[0]][p[1]] == '#')]
    for p in options:
        if not p in distances:
            continue
        if distances[p] < mind:
            mind = distances[p]

    options = {p for p in options if p in distances and distances[p] == mind}

    nextcoord = sorted(options)[0]
    #print("Nextcoord: %s"% str(nextcoord))

    return nextcoord

def attack(unit, elves, goblins):
    enimes = (elves, goblins)[unit in elves]
    units = merge(elves, goblins)
    attackable = []
    for p in adj(unit):
        if p in enimes:
            attackable.append(p)
    if len(attackable) == 0:
        return False
    # Sort by health, then by position
    opponent = sorted(attackable, key=lambda x: (enimes[x][0], x))[0]
    opponent

    enimes[opponent] = (enimes[opponent][0] - units[unit][1] , enimes[opponent][1])

    if enimes[opponent][0] <= 0:
        print("A unit is dead!")
        # enemy is dead!!
        del enimes[opponent]

    return True


def adj(c):
    return [(c[0] + 1, c[1]), (c[0] - 1, c[1]), (c[0], c[1] + 1), (c[0], c[1] - 1)]

def simulate(board, elves, goblins):
    startelves = len(elves)
    turn = 1
    while True:
        # Decide order - units cannot move outside the round so we can use a static list
        for unit in sorted([g for g in goblins] + [e for e in elves]):
            #print(unit)

            if not (unit in goblins or unit in elves):
                # unit has already died this turn
                continue

            enimes = (elves, goblins)[unit in elves]
            allies = (goblins, elves)[unit in elves]

            if attack(unit, goblins, elves):
                continue

            # move
            newcoords = move(board, elves, goblins, unit)

            allies[newcoords] = allies[unit]
            if newcoords != unit:
                del allies[unit]

            attack(newcoords, goblins, elves)

        print("After %d Rounds" %turn)
        turn+= 1
        printboard(board, elves, goblins)
        # if turn == 3:
        #     break
        if len(elves) == 0 or len(goblins) == 0:
            units = merge(elves, goblins)
            s = sum([units[u][0] for u in units])
            print(s)
            print(s * (turn-2))
            break

        if len(elves) != startelves:
            return False
    return True

def main():

    lines = []
    with open(sys.argv[1], 'r') as f:
        lines = f.read().split('\n')[:-1]


    # (HP, attack)
    goblins = {}
    elves = {}
    board = []
    for y, line in enumerate(lines):
        board.append([])
        for x, c in enumerate(line):
            board[y].append(('.','#')[c=='#'])
            if c == 'G':
                goblins[(y, x)] = (200, 3)
            elif c == 'E':
                elves[(y, x)] = (200, 3)


    for i in range(3, 200):
        elves = {e: (elves[e][0], i) for e in elves}
        print(elves)
        if simulate(board, elves.copy(), goblins.copy()):
            print(i)
            break





if __name__ == "__main__":
    main()
