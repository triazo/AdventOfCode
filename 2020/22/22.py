#!/usr/bin/python

import sys
import re
import queue

from utils import *

def copyqueue(qa, size):
    if size != qa.qsize():
        q = copyqueue(qa, qa.qsize())
    else:
        q = qa
    nq = queue.Queue()
    for i in range(size):
        x = q.get()
        q.put(x)
        nq.put(x)
    return nq

def queuelist(q):
    l = []
    for i in range(q.qsize()):
        x = q.get()
        q.put(x)
        l.append(x)
    return l

def queuestr(q):
    return " ".join(str(i) for i in queuelist(q))


rounds = 0
games = 0

allstates = {}

def execute_combat(deck1, deck2, depth, firstlevel = False):
    # if depth == 5:
    #     return 1, None

    global games
    rounds = 0
    games += 1
    d1 = deck1
    d2 = deck2
    # d1 = copyqueue(deck1)
    # d2 = copyqueue(deck2)

    l1 = queuelist(d1)
    l2 = queuelist(d2)

    if not firstlevel:
        m = max(l1 + l2)
        if m > (len(l1) + len(l2)):
            if 50 in l1:
                return 1, None
            if 50 in l2:
                return 2, None


    seen_sets = set()

    while True:
        rounds += 1
        # if (rounds %100 == 0):
        #print(rounds, games)

        state = "-".join((queuestr(d1), queuestr(d2))
        #print(state)
        if state in seen_sets:
            print(state)
            print("prventing loop, declaring p1 winner")
            return 1, d1
        seen_sets.add(state)

        if d1.qsize() == 0:
            return 2, d2
        if d2.qsize() == 0:
            return 1, d1
        c1 = d1.get()
        c2 = d2.get()

        winner = 0
        if c1 <= d1.qsize() and c2 <= d2.qsize():
            de1 = copyqueue(d1, size=c1)
            de2 = copyqueue(d2, size=c2)
            winner, winning_deck = execute_combat(de1, de2, depth + 1)
        else:
            if c1 > c2:
                winner = 1
            elif c2 > c1:
                winner = 2
            else:
                print("Cards equal, how did this happen?")
        if winner == 1:
            d1.put(c1)
            d1.put(c2)
        elif winner == 2:
            d2.put(c2)
            d2.put(c1)
        else:
            print("No winner, how did this happen?")


def main():

    sys.setrecursionlimit(2200)

    lines = getlines(2020, 22)

    onedeck = queue.Queue()
    twodeck = queue.Queue()

    active_deck = onedeck
    for l in lines[1:]:
        if l == "":
            continue
        if l.startswith("Player"):
            active_deck = twodeck
            continue
        active_deck.put(int(l))


    winner, winning_deck = execute_combat(onedeck, twodeck, 1, firstlevel = True)

    # winning_deck = None
    # if twodeck.qsize() == 0:
    #     winning_deck = onedeck
    # else:
    #     winning_deck = twodeck

    winning_list = []
    while winning_deck.qsize() != 0:
        winning_list.append(winning_deck.get())
    score = 0
    print(", ".join(str(i) for i in reversed(winning_list)))
    for i, item in enumerate(reversed(winning_list)):
        #print(i+1, item)
        score += item * (i+1)

    print(score)



if __name__ == "__main__":
    main()
