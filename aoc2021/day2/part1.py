arr=[]
with open('input.txt','r') as f:
    lines=f.readlines()
    arr=[i.strip() for i in lines]

#print(arr)
horizontal = 0
depth = 0
for line in arr:
    move,n = line.split()
    if move == "forward":
        horizontal += int(n)
    elif move == "up":
        depth -= int(n)
    elif move == "down":
        depth +=int(n)

print(horizontal*depth)



