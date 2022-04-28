
import enum


def main():
    with open('input.txt') as f:
        data=f.readline().strip()

    ds = [int(d) for d in data]
    n = len(ds)
    print(sum(d for i, d in enumerate(ds) if d == ds[(i+1) % n]))


main()