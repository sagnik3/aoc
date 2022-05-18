from collections import Counter 


def main():
    with open('input.txt','r') as f:
        p=f.read().splitlines()

    count2=0
    count3=0

    for item in p:
        count = Counter(item)
        if len([k for k,v in count.items() if v==2])>0:
            count2+=1
        if len([k for k,v in count.items() if v==3])>0:
            count3+=1

    print(count2*count3)

main()
