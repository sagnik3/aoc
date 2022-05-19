def main():
    with open('input.txt','r') as f:
        p=f.read()

    position = 0

    for key,value in enumerate(p):
        if value =='(':
            position+=1
        elif value ==')':
            position-=1

        if position == -1:
            print(key+1)
            break

main()
