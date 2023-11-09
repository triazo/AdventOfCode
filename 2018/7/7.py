#!/usr/bin/python

import sys

alphabet = 'abcdefghijklmnopqrstuvwxyz'


def main():
    lines = []
    with open(sys.argv[1], 'r') as f:
        lines = f.read().split('\n')[:-1]

    steps = {}
    for line in lines:
        s1 = line.split()[1]
        s2 = line.split()[7]
        if not s1 in steps:
            steps[s1] = ({}, {s2: ''})
        else:
            steps[s1][1][s2] = ''

        if not s2 in steps:
            steps[s2] = ({s1: ''}, {})
        else:
            steps[s2][0][s1] = ''


    result = []
    workers = [None, None, None, None, None]
    time = 0
    while len(steps) > 0:

        # ( 'P', startime )
        # Finish tasks
        for i,w in enumerate(workers):
            if not w:
                continue
            if (ord(w[0]) - ord('A')) + w[1] + 60 < time:
                result.append(w[0])
                del steps[w[0]]
                workers[i] = None

        # Find available tasks
        can_do = []
        for step in steps:
            b = True
            for s in steps[step][0]:
                if s in steps:
                    b = False
            if b:
                there = False
                for w in workers:
                    if not w:
                        continue
                    if w[0] == step:
                        there = True
                if not there:
                    can_do.append(step)

        # Start tasks
        tasks = sorted(can_do)
        while None in workers and len(tasks) > 0:
            print("worker %d is doing %s at time %d"%(workers.index(None), tasks[0], time))
            workers[workers.index(None)] = (tasks[0], time)

            del tasks[0]

        time += 1

    print (time - 1)
    print(''.join(result))



if __name__ == "__main__":
    main()
