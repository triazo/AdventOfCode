#!/usr/bin/python

import sys
import re
import queue

from utils import *

st = type("")
lt = type([])

rules = {}

def match_rule(s, i, r):
    if i >= len(s):
        return set()
    if s[i] == r:
        return {i + 1}
    if type(r) == st:
        return set()

    valid_ends = set()

    for option in r:
        temp_i = {i}
        for subrule in option:
            newis = set()
            for ti in temp_i:
                newis = newis.union(match_rule(s, ti, rules[subrule]))
            temp_i = newis
        valid_ends = valid_ends.union(temp_i)
    return valid_ends


def main():

    sys.setrecursionlimit(2200)

    lines = getlines(2020, 19, s="sampleinput2")

    rp = r"^([0-9]+): (.*)"

    for line in lines:
        if line == "":
            break
        rulenostr, rule = re.match(rp, line).groups()
        ruleno = int(rulenostr)


        if rule.startswith("\""):
            rules[ruleno] = eval(rule)
            continue

        subrules = []
        for part in rule.split("|"):
            sr = []
            for n in part.split(" "):
                if n != "":
                    sr.append(int(n))
            subrules.append(sr)

        rules[ruleno] = subrules

    rules[8] = [[42],[42, 8]]
    rules[11] = [[42,31],[42, 11, 31]]

    print(rules)
    print(len(rules))

    total = 0
    for line in lines[len(rules)-1:]:
        if line == "":
            pass

        start = rules[0]
        ends = match_rule(line, 0, start)
        if len(line) in ends:
            total += 1
        print(line, match_rule(line, 0, start))

    print(total)



if __name__ == "__main__":
    main()
