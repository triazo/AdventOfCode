#!/usr/bin/python

import sys
import re
import queue

from utils import *

def rangecheck(n, r):
    return (r[0][0] <= n and n <= r[0][1]) or (r[1][0] <= n and n <= r[1][1])

def main():

    sys.setrecursionlimit(2200)

    lines = getlines(2020, 16)

    field_regex = r"([a-z| ]+): ([0-9]+)-([0-9]+) or ([0-9]+)-([0-9]+)"

    fields = {}
    i = 0
    while i < len(lines):
        line = lines[i]
        i += 1
        if line == "":
            break
        m = re.match(field_regex, line)
        d = m.groups()
        fields[d[0]] = ((int(d[1]), int(d[2])),(int(d[3]), int(d[4])))

    i += 1 # your ticket:
    selfticket = list([int(n) for n in lines[i].split(',')])
    i += 1 # self ticket
    i += 1 # <blank line>
    i += 1 # nearby tickets:
    tickets = []
    while i < len(lines):
        line = lines[i]
        t = list([int(n) for n in lines[i].split(',')])
        i += 1

        tickets.append(t)


    invalid_error_rate = 0

    print(len(tickets))

    alltickets = tickets.copy()
    itertickets = tickets.copy()
    tickets = []

    for t in alltickets:
        startError = invalid_error_rate
        ticketgood = True
        for n in t:
            numbergood = False
            for fd in fields:
                f = fields[fd]
                numbergood = numbergood or rangecheck(n, f)

            if not numbergood:
                invalid_error_rate += n
                ticketgood = False


        # if t[1] == 990:
        #     print(ticketgood, alltickets.index(t))
        if not ticketgood:
            print(alltickets.index(t))
            #alltickets.remove(t)
            pass
        else:
            tickets.append(t)
        # if t[1] == 990:
        #     print(ticketgood, alltickets.index(t))

    print(len(tickets), len(alltickets), len(alltickets) + len(tickets))

    print("error rate (part one)", invalid_error_rate)

    #tickets.append(selfticket)

    remaining_fields = list(f for f in fields)
    #remaining_fields.remove("type")
    mns = []
    matches = []


    for i in range(len(remaining_fields)+10):
        for f in remaining_fields:
            fm = []
            for j in range(len(tickets[0])):
                if j in mns:
                    continue
                #print("checking column %d for field %s"% (j, f))
                #print(fields[f], list(t[j] for t in tickets))
                if min(rangecheck(t[j], fields[f]) for t in tickets):
                    #print("check good")
                    fm.append(j)
                elif j == 1 and f=="class":
                    for t in tickets:
                        if not rangecheck(t[j], fields[f]):
                            print(t)
                    #print(f, sum(rangecheck(t[j], fields[f]) for t in tickets), len(tickets))
            if len(fm) == 1:
                #print("field %s works for column %d"%(f, fm[0]))
                matches.append((f, fm[0]))
                mns.append(fm[0])
                remaining_fields.remove(f)

                print(f, fm[0], list(j for j in range(len(tickets[0])) if min(rangecheck(t[j], fields[f]) for t in tickets)))
                sys.stdout.write("\t\t\t\t\t\t\t\t\t")
                fm = []
                for j in range(len(tickets[0])):
                    if min(rangecheck(t[j], fields[f]) for t in tickets):
                        sys.stdout.write("X")
                    else:
                        sys.stdout.write(" ")
                sys.stdout.write('\n')


                continue
                #print(remaining_fields)


    f = "type"
    print(f, sum(min(rangecheck(t[j], fields[f]) for t in tickets) for j in range(len(tickets[0]))))
    sys.stdout.write("\t\t\t")
    fm = []
    for j in range(len(tickets[0])):
        if min(rangecheck(t[j], fields[f]) for t in tickets):
            sys.stdout.write("X")
        else:
            sys.stdout.write(" ")
    sys.stdout.write('\n')


    f = "departure station"
    print(f, sum(min(rangecheck(t[j], fields[f]) for t in tickets) for j in range(len(tickets[0]))))
    sys.stdout.write("\t\t\t")
    fm = []
    for j in range(len(tickets[0])):
        if min(rangecheck(t[j], fields[f]) for t in tickets):
            sys.stdout.write("X")
        else:
            sys.stdout.write(" ")
    sys.stdout.write('\n')

    # n = 0
    # for n in range(len(fields)):
    #     if not n in mns:
    #         n = n
    # matches.append((remaining_fields[0],n))


    total = 1
    for m in matches:
        if m[0].startswith("departure"):
            total *= selfticket[m[1]]

    print(total)

if __name__ == "__main__":
    main()
