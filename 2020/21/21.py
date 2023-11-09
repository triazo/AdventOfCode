#!/usr/bin/python

import sys
import re
import queue

from utils import *

def main():

    sys.setrecursionlimit(2200)

    lines = getlines(2020, 21)

    aller_contents = {}

    ingredients = set()

    for l in lines:
        ingred = l.split("(")[0].split(" ")[:-1]
        aller = l.split("(")[1].split(")")[0].split(" ")[1:]
        aller = list(a.replace(",","") for a in aller)

        for i in ingred:
            ingredients.add(i)

        for a in aller:
            if not a in aller_contents:
                aller_contents[a] = set(ingred)
            else:
                aller_contents[a] = aller_contents[a].intersection(set(ingred))

    for a in aller_contents:
        print(a, aller_contents[a])

    safe_ingredients = ingredients.copy()
    for a in aller_contents:
        safe_ingredients = safe_ingredients.difference(aller_contents[a])

    # print(safe_ingredients)
    # print(len(safe_ingredients))

    total = 0
    for l in lines:
        ingred = l.split("(")[0].split(" ")[:-1]
        for i in ingred:
            if i in safe_ingredients:
                total += 1

    unsolved_allergens = set(aller_contents)
    solved_allers = {}

    while len(unsolved_allergens) > 0:
        for a in unsolved_allergens:
            if len(aller_contents) == 1:
                solved_allers[a] = aller_contents.pop()


if __name__ == "__main__":
    main()
