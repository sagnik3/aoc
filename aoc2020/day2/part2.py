def main():
	with open("input.txt") as f:
		p=f.read().splitlines()

	validcount = 0  
	for item in p:
		policy,password = item.split(":")
		rangeVal,char = policy.split(" ")
		minCount,maxCount = rangeVal.split("-")
		index1=int(minCount)
		index2=int(maxCount)
		
		if (password[index1] == char and password[index2] != char) or (password[index1]!=char and password[index2]==char):
			validcount+=1 

	print(validcount)

main() 
