import numpy as np


def sum1n(n):
    return n*(n+1)/2

def main():
    with open('input.txt','r') as f:
        p=[int(x) for x in f.read().split(',')]

    meanVal = int(np.mean(p))
    res = sum([sum1n(abs(meanVal-i)) for i in p])
    print(res)

main()
