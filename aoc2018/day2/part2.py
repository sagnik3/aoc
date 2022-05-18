import fileinput

def main():
    p = [x.strip() for x in fileinput.input()]
    for line1 in p:
        for line2 in line1:
            x = ''.join(a for a , b in zip(line1,line2) if a == b)
            if len(x) == len(line1) - 1:
                return x 

print(main())

