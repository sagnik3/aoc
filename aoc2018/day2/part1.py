from collections import Counter 
import fileinput

lines = [x.strip() for x in fileinput.input()]

def main():
    has2 = 0 
    has3 = 0 

    for line in lines:
        c = Counter(line).values()
        has2 += 2 in c 
        has3 += 3 in c 
    
    print(has2*has3)


main()

