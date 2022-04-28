input_arr=[]
with open('input.txt') as f:
    input_arr = f.readline().split(',')
input_arr = [int(i) for i in input_arr]

def processArray(input_arr):
    arr = input_arr[:]

    for index in range(0,len(arr),4):
        oper = arr[index]
        numA = arr[arr[index+1]]
        numB = arr[arr[index+2]]
        if oper == 99:
            return arr[0]
        elif oper == 1:
            arr[arr[index+3]] = numA+numB
        elif oper==2:
            arr[arr[index+3]] = numA*numB
    return arr[0]

for noun in range(100):
    for verbs in range(100):
        input_arr[1] = noun
        input_arr[2] = verbs

        output  = processArray(input_arr)

        if output == 19690720:
            print(100*noun+verbs)
            break

