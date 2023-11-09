#!/usr/bin/python

import sys
import re
import queue
import collections

from utils import *

class Node():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert_after(self, a):
        self.right.left = a
        a.right = self.right
        a.left = self
        self.right = a

    def remove(self):
        self.left.right = self.right
        self.right.left = self.left
        self.left = self
        self.right = self


class CList():
    def __init__(self, startingNode):
        self.current = startingNode
        self.current.right = self.current
        self.current.left = self.current
        self.end = self.current
        self.allnodes = {self.current.data: self.current}

    def insert(self, node):
        self.current.insert_after(node)

    def insert_end(self, node):
        self.end.insert_after(node)
        self.end = node
        self.allnodes[node.data] = node

    def pop(self):
        nxt = self.current.right
        nxt.remove()
        return nxt

    def find_dest_cup(self, a, b, c):
        i = self.current.data - 1
        if i == 0:
            i = 1000000
            #i = 9
        while i == a or i == b or i == c:
            i -= 1
            if i == 0:
                i = 1000000
                #i = 9
        # scan
        #print(self.current.data, holding, i)
        return self.allnodes[i]
        # scanner = self.current
        # while scanner.data != i:
        #     scanner = scanner.left
        # return scanner

    def advance_current(self):
        self.current = self.current.right

    def __str__(self):
        items = [self.current.data]
        scanner = self.current.right
        while scanner is not self.current:
            items.append(scanner.data)
            scanner = scanner.right
        return ", ".join(str(i) for i in items)

    def get_result(self):
        scanner = self.current
        while scanner.data != 1:
            scanner = scanner.right

        one = scanner.right.data
        two = scanner.right.right.data
        print("")
        print("")
        print(one * two)


def main():

    sys.setrecursionlimit(2200)

    lines = getlines(2020, 23)

    cupslist = list(int(c) for c in lines[0])
    print(cupslist)


    cups = CList(Node(cupslist[0]))
    for cup in cupslist[1:]:
        cups.insert_end(Node(cup))

    for i in range(max(cupslist)+1, 1000001):
        cups.insert_end(Node(i))

    for rnd in range(10000000):
        # if rnd % 10000 == 0:
        #     sys.stdout.write("\r%s"%str(rnd))

        a = cups.pop()
        b = cups.pop()
        c = cups.pop()

        dest = cups.find_dest_cup(a.data, b.data, c.data)

        dest.insert_after(c)
        dest.insert_after(b)
        dest.insert_after(a)

        cups.advance_current()

        #print(cups)
    cups.get_result()

# part one 8, 9, 6, 2, 5, 1, 7, 4, 3

if __name__ == "__main__":
    main()
