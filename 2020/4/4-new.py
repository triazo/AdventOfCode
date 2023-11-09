#!/usr/bin/python

import sys
import re
import queue

from utils import *

def main():

    fields = ["byr","iyr","eyr","hgt","hcl","ecl","pid"]#,"cid"]
    sys.setrecursionlimit(2200)

    #lines = getlines(2020, 4, samplefile="sample1")
    lines = getlines(2020, 4)

    passports = []
    cur_pass = {}
    """ecl:gry pid:860033327 eyr:2020 hcl:#fffffd"""
    for l in lines:
        if l == "":
            passports.append(cur_pass)
            cur_pass = {}
            continue

        for f in l.split(" "):
            cur_pass[f.split(':')[0]] = f.split(':')[1]

    passports.append(cur_pass)



    valids = {
        "byr": r"^(19[2-8][0-9]|199[0-9]|200[0-2])$",
        "iyr": r"^(201[0-9]|2020)$",
        "eyr": r"^(202[0-9]|2030)$",
        "hcl": r"^#[0-9a-f]{6}$",
        "ecl": r"(amb|blu|brn|gry|grn|hzl|oth)",
        "pid": r"^[0-9]{9}$",
        "hgt": r"((59|6[0-9]|7[0-6])in)|((1[5-8][0-9]|19[0-3])cm)",
    }

    total = sum(min(int(re.match(valids[k], p[k]) != None) if k in p else 0 for k in valids) for p in passports)

    print(total)



if __name__ == "__main__":
    main()
