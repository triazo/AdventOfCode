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
        "bry": r"^(19[2-8][0-9]|199[0-9]|200[0-2])$",
        "iyr": r"^(201[0-9]|2020)$",
        "eyr": r"^(202[0-9]|2030)$",
        "hcl": r"^#[0-9a-f]{6}$",
        "ecl": r"(amb|blu|brn|gry|grn|hzl|oth)",
        "pid": r"^[0-9]{9}$",
        "hgt": r"",

    byrs = []
    iyrs = []
    eyrs = []
    hgts = []
    hcls = []
    ecls = []
    pids = []

    total = 0
    for p in passports:
        x = 0
        for f in fields:
            if f in p:
                x += 1


        if x != len(fields):
            continue
        if not (1920 <= int(p["byr"]) and int(p["byr"]) <= 2002):
            print("invalid byr", p["byr"])
            continue
        if not (re.match(r"^[0-9]{4}$", p["byr"])):
            print("invalid byr", p["byr"])
            continue
        byrs.append(p["byr"])

        if not (2010 <= int(p["iyr"]) and int(p["iyr"]) <= 2020):
            print("invalid iyr", p["iyr"])
            continue
        if not (re.match(r"^[0-9]{4}$", p["iyr"])):
            print("invalid byr", p["iyr"])
            continue
        iyrs.append(p["iyr"])

        if not (2020 <= int(p["eyr"]) and int(p["eyr"]) <= 2030):
            print("invalid eyr", p["eyr"])
            continue
        if not (re.match(r"^[0-9]{4}$", p["eyr"])):
            print("invalid byr", p["eyr"])
            continue

        eyrs.append(p["eyr"])

        if not (re.match("^#[0-9a-f]{6}$", p["hcl"])):
            print("invalid hcl", p["hcl"])
            continue
        hcls.append(p["hcl"])

        if not (p["ecl"] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]):
            print(p)
            print("invalid ecl", p["ecl"])
            continue
        ecls.append(p["ecl"])

        if not (re.match(r"^[0-9]{9}$", p["pid"])):
            print("invalid pid", p["pid"])
            continue
        pids.append(p["pid"])
        h = p["hgt"]
        m = re.match(r"^([0-9].+)(in|cm)$", h)
        if not m:
            #print("invalid hgt t n%s"%h, str(m.groups()))
            continue
        if m.groups()[1] == "in":
            if not (59 <= int(m.groups()[0]) and int(m.groups()[0]) <= 76):
                print("invalid hgt i %s"%h, str(m.groups()))
                continue
        if m.groups()[1] == "cm":
            if not (150 <= int(m.groups()[0]) and int(m.groups()[0]) <= 193):
                print("invalid hgt i %s"%h, str(m.groups()))
                continue
        hgts.append(p["hgt"])


        #print("valid")
        total += 1

    for b in pids:
        print(b)
    print(total)



if __name__ == "__main__":
    main()
