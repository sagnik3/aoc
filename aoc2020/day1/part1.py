arr=[]
with open('input.txt','r') as f:
    lines = f.readlines()
    for item in lines:
            arr.append(int(item))

for i in range(0,len(arr)):
    for j in range(i+1,len(arr)):
        if(arr[i]+arr[j]==2020):
            print(f"Solution : {arr[i]*arr[j]}")
            break


