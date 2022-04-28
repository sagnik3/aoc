def main():
    arr=[]
    with open('input.txt') as f:
        arr=f.readline().split(',')
    arr=[int(i) for i in arr]
    arr[1]=12
    arr[2]=2
    for i in range(0,len(arr),4):
        oper = arr[i]
        numA = arr[arr[i+1]]
        numB = arr[arr[i+2]]
        if oper == 99:
            return arr[0]
        elif oper == 1:
            arr[arr[i+3]] = numA + numB
        elif oper == 2:
            arr[arr[i+3]] = numA * numB

    return arr[0]
                  
            

if __name__=='__main__':
    print(main())
