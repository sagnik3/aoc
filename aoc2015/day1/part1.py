
def main():
    with open('input.txt','r') as f:
        p=f.read()

    currentFloor = 0 
    for i in p:
        if i=='(':
            currentFloor+=1
        elif i==')':
            currentFloor-=1
    print(currentFloor)


main()
