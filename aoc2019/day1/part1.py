#!/usr/bin/python3

# https://adventofcode.com/2019/day/1

from math import floor

def mass_to_fuel(mass):
    return floor(mass/3)-2


def main():
    with open('input.txt') as f:
        mass = [int(x) for x in f.readlines()]
    #print(mass)
    print(sum(map(mass_to_fuel,mass)))




main()


