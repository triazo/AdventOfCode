#!/usr/bin/python

import sys
import re
import queue
from functools import *

from utils import *

def combine_phased_rotations(a_period, a_phase, b_period, b_phase):
    """Combine two phased rotations into a single phased rotation

    Returns: combined_period, combined_phase

    The combined rotation is at its reference point if and only if both a and b
    are at their reference points.
    """
    gcd, s, t = extended_gcd(a_period, b_period)
    phase_difference = a_phase - b_phase
    pd_mult, pd_remainder = divmod(phase_difference, gcd)
    if pd_remainder:
        raise ValueError("Rotation reference points never synchronize.")

    combined_period = a_period // gcd * b_period
    combined_phase = (a_phase - s * pd_mult * a_period) % combined_period
    return combined_period, combined_phase


def arrow_alignment(red_len, green_len, advantage):
    """Where the arrows first align, where green starts shifted by advantage"""
    period, phase = combine_phased_rotations(
        red_len, 0, green_len, -advantage % green_len
    )
    return -phase % period

def combine_busses(b1, b2):
    return combine_phased_rotations(b1[0], b1[1], b2[0], b2[1])


def extended_gcd(a, b):
    """Extended Greatest Common Divisor Algorithm

    Returns:
        gcd: The greatest common divisor of a and b.
        s, t: Coefficients such that s*a + t*b = gcd

    Reference:
        https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm#Pseudocode
    """
    old_r, r = a, b
    old_s, s = 1, 0
    old_t, t = 0, 1
    while r:
        quotient, remainder = divmod(old_r, r)
        old_r, r = r, remainder
        old_s, s = s, old_s - quotient * s
        old_t, t = t, old_t - quotient * t

    return old_r, old_s, old_t


def check(t, busses):
    progress = 0
    for n, i in busses:
        if (t + i) % n == 0:
            progress += 1
            continue
        else:
            return progress
    return progress

def main():

    sys.setrecursionlimit(2200)

    lines = getlines(2020, 13)

    time = int(lines[0])
    busses = lines[1].split(',')

    shortest_wait = 100000000
    bid = 0
    for bc in busses:
        if bc == "x":
            continue
        b = int(bc)
        wait = -(time % b) + b
        if wait < shortest_wait:
            shortest_wait = wait
            bid = b

    print(shortest_wait, bid)
    print(shortest_wait * bid)

    # pre-enumerate
    prebusses = []
    for i, b in enumerate(busses):
        if b == "x":
            continue
        prebusses.append((int(b), i))


    print(prebusses)
    # try out multiples

    accumulator = prebusses[0]
    for bus in prebusses[0:]:
        accumulator = combine_busses(accumulator, bus)
        print("combined_phases", accumulator)

    a1 = accumulator[0]
    a2 = accumulator[1]
    print(-1* (a2 - a1))

    busses_sorted = list(sorted([int(x) for x in filter(lambda x: x != "x", busses)]))
    print(busses_sorted)
    # lcm = 1
    # for b in busses_sorted:
    #     lcm = compute_lcm(lcm, b)

    # print("lcm", lcm)



    mb = max([int(x) if x != "x" else 0 for x in busses])
    t = mb - busses.index(str(mb))
    print(t)

    inc = int(busses[0])
    inc = 1
    t = 0
    progress = 0
    progstart = 0
    iters = 0
    checkres = 0
    while checkres < len(busses_sorted):
        iters += 1
        #print(inc)
        checkres = check(t, prebusses)
        #print(checkres, t)
        # if checkres == True:
        #     break
        if checkres > progress:
            print("prog check", t, progstart, progress, inc)
            if progstart != 0:
                inc = t - progstart
                progress = checkres
                t = progstart
                progstart = 0
                print("progress", progress, inc)
            else:
                progstart = t
        t += inc
        #sys.stdout.write("%d\r"%t)

    print("solution", t, iters)


if __name__ == "__main__":
    main()
