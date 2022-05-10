#balencing parenthesis problem , using a stack to solve it 

open_list = ["[","{","(","<"]
close_list = ["]","}",")",">"]
		
class Stack:
	def __init__(self):
		stack=[]

	def check(self,inputString):
		
		for i in inputString:
			if i in self.open_list:
				stack.append(i)
			elif i in self.close_list:
				pos = self.close_list.index(i)
				if((len(stack)>0)) and (self.open_list[pos]==stack[len(stack)-1]):
					stack.pop()
				else:
					#return a tuple of the brace that was unbalanced 
					return "Unbalanced",stack[len(stack)-1]

		if len(stack) == 0:
			return "Balanced"
		else:
			return "Unbalanced",stack[len(stack)-1]

	def checkCorrupted(self,inputString):
		corruptStatus=False 
		for item in inputString:
			a= open_list.count(item) 
			b= close_list.count(item)
			if a==0 or b==0:
				corruptStatus=True
				break
		return corruptStatus


def main():
	with open("input.txt","r") as f:
		p=f.read().splitlines()

	score = 0 
	for line in p:
		#clearing out the corrupted ones 
		if Stack().checkCorrupted(line):
			p.remove(line)
	
	#get syntax error count and the score 
	for line in p:
		

main()
