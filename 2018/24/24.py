#!/usr/bin/python

import sys
import re
import regex
import queue
import pulp
import itertools

alphabet = 'abcdefghijklmnopqrstuvwxyz'

class Group():
    def __init__(self, units, hp, attack, affinity, initiative, immune, weak):
        self.units = int(units)
        self.hp = int(hp)
        self.attack = int(attack)
        self.affinity = affinity
        self.initiative = int(initiative)
        self.immune = immune
        self.weak = weak

    def __repr__(self):
        return str(self.units)




def mod(num, length):
    if num < 0:
        return num + length
    return num % length

def vadd(a, b):
    return (a[0] + b[0], a[1] + b[1])

def distance(a, b):
    s = 0
    for i in range(len(a)):
        s += abs(a[i] - b[i])
    return s


def initilize_groups(lines):
    immune_groups = []
    infection_groups = []
    curlist = []
    for line in lines:
        if 'Immune' in line:
            curlist=immune_groups
            continue
        if 'Infection' in line:
            curlist=infection_groups
            continue
        if line == '':
            continue
        mr = r'([0-9]+) units each with ([0-9]+) hit points (?:\((.+)\) )?with an attack that does ([0-9]+) ([a-z]+) damage at initiative ([0-9]+)'
        units, hp, wimmune, attack, affinity, initiative = re.search(mr, line).groups()

        wr = r'(?:immune to ([a-z, ]+))?;?(?:weak to ([a-z, ]+))?'
        immune = []
        weak = []

        if wimmune:
            m = regex.search(wr, wimmune).groups()
            if m[0]:
                immune = m[0].split(', ')
            if m[1]:
                weak = m[1].split(', ')
        curlist.append(Group(units, hp, attack, affinity, initiative, immune, weak))

    return immune_groups, infection_groups

def main():

    sys.setrecursionlimit(2200)

    lines = []
    with open(sys.argv[1], 'r') as f:
        lines = f.read().split('\n')[:-1]

    immune_groups, infection_groups = initilize_groups(lines)
    print(immune_groups)
    print(infection_groups)

if __name__ == "__main__":
    main()
