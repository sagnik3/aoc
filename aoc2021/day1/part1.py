arr = []
with open('input.txt','r') as f:
    lines = f.readlines()
    arr=[int(i) for i in lines]

print(sum(a<b for a,b in zip(arr,arr[1:])))


