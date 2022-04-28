arr=[]
with open('input.txt','r') as f:
    lines=f.readlines()
    arr=[int(i) for i in lines]

## for making the windows sizes
windows = list(zip(arr,arr[1:],arr[2:]))

print(sum(sum(a)<sum(b) for a,b in zip(windows,windows[1:])))

