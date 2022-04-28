arr=[]
with open('input.txt','r') as f:
    lines=f.readlines()
    arr=[i.strip() for i in lines]

h = 0
a = 0
d = 0

for line in arr:
    move,n = line.split()
    if move == "forward":
        h += int(n)
        d += int(n) * a
    elif move == "up":
        a -= int(n)
    elif move == "down":
        a += int(n)

print(h*d)
