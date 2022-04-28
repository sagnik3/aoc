arr =[]

with open('input.txt','r') as f:
    lines = f.readlines()
    for i in lines:
        arr.append(i.strip('\n'))

freq = 0
for i in arr:
    if(i[0]=='+'):
        val=int(i[1:])
        freq+=val
    elif(i[0]=='-'):
        val=int(i[1:])
        freq-=val

print(freq)
