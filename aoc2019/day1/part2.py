#!/usr/bin/python3 

#https://adventofcode.com/2019/day/1#part2

from math import floor

def mass_to_fuel(mass):
    return floor(mass/3)-2

def main():
    with open('input.txt') as f:
        mass=[int(x) for x in f.readlines()]
    
    c = 0 
    for m in mass:
        while m> 0:
            m = max(0,mass_to_fuel(m))
            c += m
    print(c)

main()
