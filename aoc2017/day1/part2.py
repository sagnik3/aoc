def main():
    p=[]
    with open('input.txt') as f:
        p=f.readline().strip()

    ds = [int(d) for d in p]
    n = len(ds)
    
    #part2
    print(sum(d for i,d in enumerate(ds) if d == ds[(i+n//2)%n]))

if __name__=='__main__':
    main()