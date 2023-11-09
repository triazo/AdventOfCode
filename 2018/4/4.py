#!/usr/bin/python

import sys

def main():
    lines = []
    with open(sys.argv[1], 'r') as f:
        lines = f.read().split('\n')[:-1]
        
    guardtotals = {}
    guardtimes = {}
    guardtimes[0] = []
    for i in range(60):
        guardtimes[0].append(0)

    sleepstart = 0
    guard = 0
    events = []
    for l in lines:
        year = l.split('[')[1].split('-')[0]
        month = l.split('[')[1].split('-')[1]
        day = l.split('[')[1].split('-')[2].split(' ')[0]
        hour = l.split('[')[1].split('-')[2].split(' ')[1].split(':')[0]
        minute = int(l.split('[')[1].split('-')[2].split(' ')[1].split(':')[1].split(']')[0])

        events.append((year, month, day, hour, minute, l))

        #print(year, month, day, hour, minute)

    events = sorted(events)

    for e in events:
        print(e)
        l = e[5]
        minute = e[4]
        if l[19:].startswith('Guard'):
            number = int(l.split(' ')[3][1:])
            #print(number)
            guard = number
            if not guard in guardtotals:
                guardtotals[guard]=0
                guardtimes[guard]=[]
                for i in range(60):
                    guardtimes[guard].append(0)
                    
        elif l[19:].startswith('falls'):
            sleepstart = minute
        elif l[19:].startswith('wakes'):
            if guard == 0:
                continue
            sleepend = minute
            guardtotals[guard]+=sleepend - sleepstart
            for m in range(sleepstart, sleepend):
                guardtimes[guard][m]+=1
                
    sg = 0
    guardtotals[0] = 0
    print(guardtotals)
    for g in guardtotals:
        if guardtotals[g] > guardtotals[sg]:
            sg = g
            
    print(sg)

    maxtime = 0
    for i in range(60):
        if guardtimes[sg][i] > guardtimes[sg][maxtime]:
            maxtime = i
    #maxtime = guardtimes[sg].index(max(guardtimes[sg]))
    print(guardtimes[sg])
    print(maxtime)
    print(sg * maxtime)

    mg = 0
    mi = 0
    for g in guardtimes:
        if g == 0: continue
        for i in range(60):
            if guardtimes[g][i] > guardtimes[mg][mi]:
                mg = g
                mi = i
    print (mg * mi)

if __name__ == "__main__":
    main()

