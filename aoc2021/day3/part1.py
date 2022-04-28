arr = []
with open('input.txt','r') as f:
    lines = f.readlines()
    arr=[i.strip() for i in lines]

#print(arr)
t=list(zip(*arr))
gamma = "".join("1" if column.count("1") > column.count("0") else "0" for column in t)
epsilon = "".join("1" if column.count("1") < column.count("0") else "0" for column in t)


#return to decimal(from binary) and print
print(int(gamma,2)*int(epsilon,2))

