from functools import reduce

def checkAnagram(words):
	s=set()
	for item in words:
		item = reduce(lambda x,y : x+y,sorted(item))
		print(item)
		s.add(item)
	if len(s) == len(words) :
		return False 
	else:
		return True 

def sanitycheck():
	#print(checkAnagram(["abcde","fghij"]))
	print(checkAnagram(["abcde","xyz","ecdab"]))
	print(checkAnagram(["a","ab","abc","abd","abf","abj"]))
	print(checkAnagram(["iiii","oiii","ooii","oooi","oooo"]))
	#print(checkAnagram(["oiii","ioii","iioi","iiio"]))

sanitycheck()


def main():
	with open("input.txt") as f:
		q=f.readlines()
	
	q=[i.strip() for i in q]
	count = 0 
	for item in q:
		#s=set()
		tokens=item.split(" ")
		ideal = len(tokens)
		#for i in tokens:
		#	s.add(i)
		if(checkAnagram(tokens)==False):
			count+=1

	print(count)

main()