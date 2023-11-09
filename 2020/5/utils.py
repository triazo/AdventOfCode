#!/usr/bin/python

import sys
import re
import queue
import requests

alphabet = 'abcdefghijklmnopqrstuvwxyz'

def getlines(year, number, s=""):
    cookies = {"session": "53616c7465645f5f0457c13656d13ca45b713be2cacb74c62d445b7b3ce833ba3b936065906cc8f9d315600b22c25cf9"}
    try:
        filename = "input" if s == "" else s
        f = open(filename)
        lines = f.read().split('\n')[:-1]
        f.close()
        return lines
    except IOError:
        if s != "":
            print("samplefile %s not found"%s)
            sys.exit(1)
        inlines = requests.get("https://adventofcode.com/%d/day/%d/input"%(year, number), cookies = cookies)
        if not inlines.ok:
            print("Request bad: %d"%inlines.status_code)
            sys.exit(1)
        with open("input", "w") as f:
            f.write(inlines.content.decode('utf-8'))
        return  inlines.content.decode('utf-8').split('\n')[:-1]


def mod(num, length):
    if num < 0:
        return num + length
    return num % length

def vadd(a, b):
    return (a[0] + b[0], a[1] + b[1])
