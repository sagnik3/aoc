
def part1(s:str) -> int:
    lines = s.splitlines()
    x,y=0,0

    count = 0
    x +=3 
    x %= len(lines[0])
    y +=1
    while y< len(lines):
        if lines[y][x] =="#":
            count+=1
        x +=3
        x %= len(lines[0])
        y +=1
    return count 

def main():
    with open('input.txt') as f:
        print(part1(f.read()))


if __name__=='__main__':
    main()


