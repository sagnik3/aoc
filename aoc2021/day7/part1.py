import numpy as np


def main():
    with open('input.txt') as f:
        p=f.read().split(',')
    p=[int(x) for x in p]
    median = np.median(p)
    result = [sum([abs(median-i) for i in p])]
    print(result)


main()

