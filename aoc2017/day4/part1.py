def main():
	with open("input.txt") as f:
		q=f.readlines()
	
	q=[i.strip() for i in q]
	count = 0 
	for item in q:
		s=set()
		tokens=item.split(" ")
		ideal = len(tokens)
		for i in tokens:
			s.add(i)
		if(len(s)==ideal):
			count+=1

	print(count)


main()
