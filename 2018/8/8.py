#!/usr/bin/python

import sys

alphabet = 'abcdefghijklmnopqrstuvwxyz'

def count(start, ints):
    children = ints[start]
    metadata = ints[start+1]

    # Get children
    diff = 2
    metasum = 0
    childmetas = []
    for i in range(children):
        cmeta, cdiff = count(start + diff, ints)
        diff += cdiff
        childmetas.append(cmeta)

    # Get metadata
    for i in range(metadata):
        if children == 0:
            print("No children: adding %d"%ints[start + diff])
            metasum += ints[start + diff]
        if (ints[start + diff]-1) < len(childmetas):
            print("Children: adding %d"%ints[start + diff])
            metasum += childmetas[ints[start + diff] - 1]
        diff += 1

    print("Metasum of %d is %d"%(start, metasum))
    return (metasum, diff)


def main():
    lines = []
    with open(sys.argv[1], 'r') as f:
        lines = f.read().split('\n')[:-1]

    #((children, metadata), children, metadata)
    depth = 0
    nodes = []

    ints = [int(i) for i in lines[0].split()]
    diff, metasum = count(0, ints)
    print(diff, metasum)

if __name__ == "__main__":
    main()
