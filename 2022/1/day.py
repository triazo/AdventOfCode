#!/usr/bin/python

import sys

masterlist = open(sys.argv[1],'r').read().split('\n')
highest_calories = 0
elftotal = 0

totals = []

for item in masterlist:
    if item == "":
        totals.append(elftotal)
        # print(elftotal)
        elftotal = 0
        # if elftotal > highest_calories:
        continue
    elftotal = int(item) + elftotal

print(max(totals))

sorted_list = sorted(totals)
cut_list = sorted_list[-3:]
print(sum(cut_list))
